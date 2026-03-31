# -*- coding: utf-8 -*-
import os

# DMG settings for dmgbuild

# Format: ULFO (LZMA compression, macOS 10.15+)
format = 'ULFO'

# Compression level (1-9, higher = smaller but slower)
compression_level = 9

# Volume name
volume_name = 'OpenClaw桌面版'

# Icon size and position
icon_size = 96
icon_locations = {
    'OpenClaw.app': (140, 120),
    'Applications': (500, 120),
}

# Background
background = None

# Window size
window_rect = ((100, 100), (640, 380))

# Icon view settings
icon_view_settings = {
    'iconSize': icon_size,
    'arrangeBy': 'none',
}

# Create Applications symlink
files = [
    ('OpenClaw.app', 'OpenClaw.app'),
]

# Symlinks
symlinks = {
    'Applications': '/Applications',
}
