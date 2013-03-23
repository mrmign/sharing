'''
Bookmark processing
Kristjan Kannike
Created: 2005-06-04
Changed: 2009-06-30

Clean up Firefox bookmarks (remove non-standard attributes, esp. ICON), with
the exception of FEEDURL, and make it into a well-formed XHTML file.
Set correct heading levels.

It can be used from the command line as

python bookmarks.py bookmarks.html [cleanedBookmarksFilename.html]
'''

import re
from htmlentitydefs import name2codepoint
from os.path import splitext


def fromName2codepoint(string):
    '''String with (X)HTML entitites -> string with their Unicode counterparts.

    >>> fromName2codepoint('This &amp; that.')
    'This &#38; that.'

    '''
    for key, val in name2codepoint.iteritems():
        string = string.replace('&%s;' % key, '&#%d;' % val)
    return string


def cleanBookmarks(content, newFilename=None):
    '''Firefox bookmarks -> cleaned up bookmarks in an XHTML file'''
    # bm = file(filename, 'r')
    # bmCont = bm.read()
    # bm.close()
    bmCont = content
    # Correct heading levels
    bmContLines = bmCont.split('\n')
    headingLevel = 1
    for i in range(0, len(bmContLines)):
        if '<DL>' in bmContLines[i]:
            headingLevel += 1
        if '</DL>' in bmContLines[i]:
            headingLevel -= 1
        bmContLines[i] = \
            bmContLines[i].replace('<H3', '<h%d' % headingLevel)
        bmContLines[i] = \
            bmContLines[i].replace('</H3', '</h%d' % headingLevel)
    bmCont = '\n'.join(bmContLines)

    # Simple cleanup substitutions
    bmSubs = {'<!DOCTYPE NETSCAPE-Bookmark-file-1>': '',
              '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">': '',
              '<TITLE>Bookmarks</TITLE>': '',
              ' >': '>',
              '<H1': '<h1',
              '</H1': '</h1',
              '<DL>': '',
              '</DL>': '',
              '<P>': '',
              '<p>': '',
              'updated null': '',
              'error null': '',
              '<DT>': '',
              '</DT>': '',
              '<A ': '<p><a ',
              '</A>': '</a></p>',
              'HREF': 'href',
              'FEEDURL': 'feedurl',
              '<HR>': '<hr />',
              ' -> ': ' -&gt; '
              }

    for sub, repl in bmSubs.iteritems():
        bmCont = bmCont.replace(sub, repl)

    bmCont = fromName2codepoint(bmCont)

# Cleanup substitution patterns for regexes
    reSubsInBM = {
        '<DD>.*?\n': '',
        ' ADD_DATE="[^"]*"': '',
        ' LAST_MODIFIED="[^"]*"': '',
        'PERSONAL_TOOLBAR_FOLDER="true"': '',
        ' ID="[^"]*"': '',
        ' LAST_VISIT="[^"]*"': '',
        'ICON="[^"]*"': '',
        'ICON_URI="[^"]*"': '',
        ' LAST_CHARSET="[^"]*"': '',
        '<script.*?</script>': '',  # Esp. the JavaScript shell
        '<style.*?</style>': '',
        r'(no-)?(updated|error) \[.*?\]': '',  # From Sage the Firefox RSS reader
        '&(?!#)': '&amp;',  # Unencoded &'s
        '<p><a href="javascript.*?<html.*?</html>.*?</a></p>': ''  # The JS Shell
    }

    for pat, repl in reSubsInBM.iteritems():
        pattern = re.compile(pat, re.DOTALL)
        bmCont = pattern.sub(repl, bmCont)

    # Add proper XHTML file beginning and ending
    before = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Bookmarks</title>
</head>

<body>'''
    after = '''</body>
</html>'''
    bmCont = before + bmCont + after

    return bmCont

    # if newFilename is not None:
    #     bmNew = file(newFilename, 'w')
    # else:
    #     (root, ext) = splitext(filename)
    #     bmNew = file(root+'_CLEANED'+ext, 'w')
    # bmNew.write(bmCont)
    # bmNew.close()
