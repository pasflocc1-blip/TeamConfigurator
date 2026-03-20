# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('frontend_dist', 'frontend_dist'),
    ],
    hiddenimports=[
        # uvicorn
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
        # anyio
        'anyio',
        'anyio._backends._asyncio',
        # sqlalchemy
        'sqlalchemy.dialects.sqlite',
        'sqlalchemy.sql.default_comparator',
        # app modules — FONDAMENTALE per PyInstaller
        'database',
        'models',
        'schemas',
        'routers',
        'routers.teams',
        'routers.registry',
        'routers.debug',
        # pydantic
        'pydantic',
        'pydantic.deprecated.class_validators',
        'pydantic.v1',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='TeamConfigurator',
    debug=False,
    strip=False,
    upx=True,
    console=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='TeamConfigurator',
)

app = BUNDLE(
    coll,
    name='TeamConfigurator.app',
    icon=None,
    bundle_identifier='com.tuonome.teamconfigurator',
    info_plist={
        'NSHighResolutionCapable': True,
        'LSBackgroundOnly': False,
    },
)
