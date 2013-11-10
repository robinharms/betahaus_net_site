# -*- coding: utf-8 -*-
from os.path import join
from pkg_resources import resource_filename

from pyramid.response import Response
from pyramid.view import view_config
from kotti.interfaces import INavigationRoot
from kotti.resources import get_root
from kotti.security import has_permission


_favicon = open( resource_filename('betahaus_net_site', 'static/favicon.ico') ).read()

#_favicon = open(join( resource_filename('voteit.core', ''), 'static', 'favicon.ico')).read()
_fi_response = Response(content_type='image/x-icon',
                        body=_favicon)


@view_config(name='favicon.ico')
def favicon_view(context, request):
    return _fi_response

# 
# @view_config(name='local-navigation',
#              renderer='kotti:templates/view/nav-local.pt')
# def local_navigation(context, request):
# 
#     def ch(node):
#         return [child for child in node.values()
#                 if child.in_navigation and
#                 has_permission('view', child, request)]
# 
#     parent = context
#     children = ch(context)
#     if not children and context.__parent__ is not None:
#         parent = context.__parent__
#         children = ch(parent)
#     if len(children) and parent != get_root() and not \
#             INavigationRoot.providedBy(parent):
#         return dict(parent=parent, children=children)
#     return dict(parent=None)
# 
# 
# def includeme_local_navigation(config):
#     # Import is needed in function scope to resolve circular imports caused by
#     # compatibility imports in slots.py.
#     from kotti.views.slots import assign_slot
#     config.scan(__name__)
#     assign_slot('local-navigation', 'right')
