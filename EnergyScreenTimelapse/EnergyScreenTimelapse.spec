# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['EnergyScreenTimelapse.py'],
             pathex=['C:\\Users\\mathe\\Documents\\C\\coding\\energy screen timelapse\\Energy\\EnergyScreenTimelapse'],
             binaries=[],
             datas=[('C:\\Users\\mathe\\Documents\\C\\coding\\energy screen timelapse\\Energy\\EnergyScreenTimelapse\\eel\\eel.js', 'eel'), ('web', 'web')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='EnergyScreenTimelapse',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='EnergyScreenTimelapse')
