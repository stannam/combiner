import os

def genHtml(title, img_name, numbering, by_directory=False, is_last=False):
    """
    generate in html format. returns a list composed of each line of html
    :param title: str. title provided by the user
    :param img_name: str. name of the img file
    :param numbering: int. the numbering of the episode
    :param by_directory: bool. whether the user selected is directory
    :param is_last: bool. whether the last episode
    :return: list of html
    """

    is_first = True if numbering == 1 else False

    # html header
    line = ['<html>', '<head>', '<title>', title, '</title>',
            '</head>', '<body style="margin:0;padding:0" bgcolor="White">']

    # visible header where the user nativates to previous or next episode
    navigate = ['<center>']
    if not is_first:
        prev = str(numbering-1)+'화'
        navigate.append('<a href="./{}.html">{}</a> &nbsp;&nbsp;&nbsp;&nbsp;'.format(prev, prev+' <<<'))

    navigate.append('<b>{} {}</b>&nbsp;&nbsp;&nbsp;&nbsp;'.format(title, str(numbering)+'화'))

    if not is_last:
        next = str(numbering + 1) + '화'
        navigate.append('<a href="./{}.html">{}</a>'.format(next, '>>> '+next))

    navigate.append('</center>')

    line = line + navigate

    # present the image files
    if not by_directory:
        line.append('<p align=center><img src="../{}" style="max-width:1000;"></p>'.format(img_name))

    ### visible footer where the user nativates to previous or next episode. simply repeating the header
    line = line + navigate

    ### html footer
    line + ['</body>', '</html>']

    return line

def writeHTML(numbering, html, path):
    """
    export as html file
    :param numbering: int. the numbering of the episode
    :param html: a list of html lines.
    :param path: path to which the generated html file is exported.
    :return:
    """
    viewerDir = path+'/_viewer/'
    htmlPath = viewerDir+str(numbering)+'화.html'

    # Create the viewer directory
    try:
        os.mkdir(viewerDir)
    except FileExistsError:
        pass

    with open(htmlPath, 'w', encoding='UTF-8') as f:
        for line in html:
            f.write(line+'\n')
