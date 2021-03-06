# -*- mode: python -*-
a = Analysis(['scripts/cb-threatconnect-connector'],
             pathex=['.'],
             hiddenimports=['unicodedata',
                            'parsedatetime.pdt_locales.de_DE',
                            'parsedatetime.pdt_locales.en_AU',
                            'parsedatetime.pdt_locales.en_US',
                            'parsedatetime.pdt_locales.es',
                            'parsedatetime.pdt_locales.nl_NL',
                            'parsedatetime.pdt_locales.pt_BR',
                            'parsedatetime.pdt_locales.ru_RU',
                            'parsedatetime.pdt_locales.fr_FR',
                            'tcex.tcex_resources'],
             datas=[ (HOMEPATH + '/cbapi/response/models/*', 'cbapi/response/models/'),
                     (HOMEPATH + '/cbapi/protection/models/*', 'cbapi/protection/models/'),
                     (HOMEPATH + '/cbapi/defense/models/*', 'cbapi/defense/models/') ],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='cb-threatconnect-connector',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='cb-threatconnect-connector')
