# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Virtue.py'],
             pathex=['C:\\Users\\Karan\\AppData\\Local\\Programs\\Python\\Python39\\Scripts'],
             binaries=[],
			 datas=[],
             hiddenimports=['pkg_resources.py2_warn', 'dependency_injector.errors', 'six','pyttsx3.drivers','pyttsx3.drivers.dummy','pyttsx3.drivers.espeak','pyttsx3.drivers.nsss','pyttsx3.drivers.sapi5'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
			 

a.datas += Tree('D:/PROJECTS/VirtualAssistant/DataBase/UIX/', prefix='DataBase/UIX')	
	
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='virtue',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon='D:\\PROJECTS\\VirtualAssistant\\DataBase\\UIX\\icon_2.ico')
		  