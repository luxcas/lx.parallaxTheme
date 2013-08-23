from plone.theme.interfaces import IDefaultPloneLayer


class ILxParallaxTheme(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "Lx Parallax Scrolling Theme" theme, this interface must be its layer
       (in parallaxTheme/viewlets/configure.zcml).
    """
