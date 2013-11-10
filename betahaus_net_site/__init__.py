from pyramid.i18n import TranslationStringFactory
from fanstatic import Library
from fanstatic import Resource
from kotti.fanstatic import edit_needed
from kotti.fanstatic import view_needed
from kotti.fanstatic import base_css

PROJECTNAME = 'betahaus_net_site'
BetahausTSF = TranslationStringFactory(PROJECTNAME)

betahaus_net_lib = Library('betahaus_static', 'static')
main_css = Resource(betahaus_net_lib, 'main.css', depends = (base_css,))


view_needed.add(main_css)
edit_needed.add(main_css)

def includeme(config):
    cache_ttl_seconds = int(config.registry.settings.get('cache_ttl_seconds', 7200))
    config.add_static_view('static', '%s:static' % PROJECTNAME, cache_max_age = cache_ttl_seconds)
    config.scan()


def kotti_configure(settings):
    settings['kotti.fanstatic.view_needed'] = '%s.view_needed' % PROJECTNAME
    settings['kotti.fanstatic.edit_needed'] = '%s.edit_needed' % PROJECTNAME
