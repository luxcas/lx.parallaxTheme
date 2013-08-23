# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.memoize.instance import memoize


class LxFolderFullView(BrowserView):
    """ view
    """

    __call__ = ViewPageTemplateFile('templates/lxfolderfullview.pt')

    @memoize
    def getContent(self):
        context = self.context
        contentFolder = context.folderlistingFolderContents()
        contents = []
        for item in contentFolder:
            if (item.portal_type == 'News Item') or (item.portal_type == 'Document'):
                contents.append(item)
        return contents
