import os
import wave
import json
import glob
import re
def crete():
    date={
    "FilePath":os.getcwd()+"project.ymmp",
    "Timeline": {
        "VideoInfo": {
            "FPS": 30,
            "Hz": 48000,
            "Width": 1920,
            "Height": 1080
        },
        "VerticalLine": {
            "IsEnabled": False,
            "StartFrame": 0,
            "LineType": "BPM",
            "Line": {
                "$type": "YukkuriMovieMaker.Project.VerticalBPMLine, YukkuriMovieMaker.Plugin",
                "BPM": 100
            },
            "Group": 4
        },
        "Items": [],
        "LayerSettings": {
            "Items": []
        },
        "CurrentFrame": 0,
        "Length": 1,
        "MaxLayer": 0
    },
    "Characters": [],
    "CollapsedGroups": []
    }
    return date

def crete_audio(file,frame=0,layer=0,length=10):
    
    data={
    "$type": "YukkuriMovieMaker.Project.Items.AudioItem, YukkuriMovieMaker",
    "IsWaveformEnabled": False,
    "FilePath": os.path.abspath(file),
    "AudioTrackIndex": 0,
    "Volume": {
        "Values": [
        {
            "Value": 50.0
        },
        {
            "Value": 0.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "Pan": {
        "Values": [
        {
            "Value": 0.0
        },
        {
            "Value": 0.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "PlaybackRate": 100.0,
    "ContentOffset": "00:00:00",
    "FadeIn": 0.0,
    "FadeOut": 0.0,
    "IsLooped": False,
    "EchoIsEnabled": False,
    "EchoInterval": 0.1,
    "EchoAttenuation": 40.0,
    "AudioEffects": [],
    "Group": 0,
    "Frame": frame,
    "Layer": layer,
    "KeyFrames": {
        "Frames": [],
        "Count": 0
    },
    "Length": length,
    "Remark": "",
    "IsLocked": False,
    "IsHidden": False
    }
    return data
def crete_Text(serif,size=34,ue_kankak=100,yoko_kankak=0,frame=0,layer=0,length=10,font="メイリオ"):
    data={
        "$type": "YukkuriMovieMaker.Project.Items.TextItem, YukkuriMovieMaker",
        "Text":serif,
        "Decorations": [],
        "Font":font,
        "FontSize": {
          "Values": [
            {
              "Value": size
            }
          ],
          "Span": 0.0,
          "AnimationType": "なし"
        },
        "LineHeight2": {
          "Values": [
            {
              "Value": ue_kankak
            }
          ],
          "Span": 0.0,
          "AnimationType": "なし"
        },
        "LetterSpacing2": {
          "Values": [
            {
              "Value": yoko_kankak
            }
          ],
          "Span": 0.0,
          "AnimationType": "なし"
        },
        "DisplayInterval": 0.0,
        "WordWrap": "NoWrap",
        "MaxWidth": {
          "Values": [
            {
              "Value": 1920.0
            }
          ],
          "Span": 0.0,
          "AnimationType": "なし"
        },
        "BasePoint": "LeftTop",
        "FontColor": "#FFFFFFFF",
        "Style": "Normal",
        "StyleColor": "#FF000000",
        "Bold": False,
        "Italic": False,
        "IsDevidedPerCharacter": False,
        "X": {
          "Values": [
            {
              "Value": 0.0
            }
          ],
          "Span": 0.0,
          "AnimationType": "なし"
        },
        "Y": {
          "Values": [
            {
              "Value": 0.0
            }
          ],
          "Span": 0.0,
          "AnimationType": "なし"
        },
        "Z": {
          "Values": [
            {
              "Value": 0.0
            }
          ],
          "Span": 0.0,
          "AnimationType": "なし"
        },
        "Opacity": {
          "Values": [
            {
              "Value": 100.0
            }
          ],
          "Span": 0.0,
          "AnimationType": "なし"
        },
        "Zoom": {
          "Values": [
            {
              "Value": 100.0
            }
          ],
          "Span": 0.0,
          "AnimationType": "なし"
        },
        "Rotation": {
          "Values": [
            {
              "Value": 0.0
            }
          ],
          "Span": 0.0,
          "AnimationType": "なし"
        },
        "FadeIn": 0.0,
        "FadeOut": 0.0,
        "Blend": "Normal",
        "IsInverted": False,
        "IsClippingWithObjectAbove": False,
        "IsAlwaysOnTop": False,
        "IsZOrderEnabled": False,
        "VideoEffects": [],
        "Group": 0,
        "Frame": frame,
        "Layer": layer,
        "KeyFrames": {
          "Frames": [],
          "Count": 0
        },
        "Length": length,
        "PlaybackRate": 100.0,
        "ContentOffset": "00:00:00",
        "Remark": "",
        "IsLocked": False,
        "IsHidden": False
      }
    return data


def crete_Voice(serif,charc):
    deta={
    "$type": "YukkuriMovieMaker.Project.Items.VoiceItem, YukkuriMovieMaker",
    "IsWaveformEnabled": False,
    "CharacterName":charc,
    "Serif": serif,
    "Decorations": [],
    "Hatsuon": "",
    "Pronounce": None,
    "VoiceLength": "00:00:00",
    "VoiceCache": None,
    "Volume": {
        "Values": [
        {
            "Value": 50.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "Pan": {
        "Values": [
        {
            "Value": 0.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "PlaybackRate": 100.0,
    "VoiceParameter": {
        "$type": "YukkuriMovieMaker.Voice.VoiceParameter, YukkuriMovieMaker",
        "Speed": 120
    },
    "ContentOffset": "00:00:00",
    "VoiceFadeIn": 0.0,
    "VoiceFadeOut": 0.0,
    "EchoIsEnabled": False,
    "EchoInterval": 0.1,
    "EchoAttenuation": 40.0,
    "AudioEffects": [],
    "JimakuVisibility": "UseCharacterSetting",
    "Y": {
        "Values": [
        {
            "Value": 0.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "X": {
        "Values": [
        {
            "Value": 530.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "Z": {
        "Values": [
        {
            "Value": 0.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "Opacity": {
        "Values": [
        {
            "Value": 100.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "Zoom": {
        "Values": [
        {
            "Value": 100.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "Rotation": {
        "Values": [
        {
            "Value": 0.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "JimakuFadeIn": 0.0,
    "JimakuFadeOut": 0.0,
    "Blend": "Normal",
    "IsInverted": False,
    "IsClippingWithObjectAbove": False,
    "IsAlwaysOnTop": False,
    "IsZOrderEnabled": False,
    "Font": "メイリオ",
    "FontSize": {
        "Values": [
        {
            "Value": 45.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "LineHeight2": {
        "Values": [
        {
            "Value": 100.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "LetterSpacing2": {
        "Values": [
        {
            "Value": 0.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "DisplayInterval": 0.0,
    "WordWrap": "NoWrap",
    "MaxWidth": {
        "Values": [
        {
            "Value": 1920.0
        }
        ],
        "Span": 0.0,
        "AnimationType": "なし"
    },
    "BasePoint": "CenterBottom",
    "FontColor": "#FFFFFFFF",
    "Style": "Border",
    "StyleColor": "#FF0FCF00",
    "Bold": False,
    "Italic": False,
    "IsDevidedPerCharacter": False,
    "JimakuVideoEffects": [],
    "TachieFaceParameter": None,
    "TachieFaceEffects": [],
    "Group": 0,
    "Frame": 0,
    "Layer": 1,
    "KeyFrames": {
        "Frames": [],
        "Count": 0
    },
    "Length": 63,
    "Remark": "",
    "IsLocked": False,
    "IsHidden": False
    }
    return deta

def get_wav_duration(file_path):
    with wave.open(file_path, 'rb') as wave_file:
        # フレーム数を取得
        frames = wave_file.getnframes()
        # サンプリングレートを取得
        frame_rate = wave_file.getframerate()
        # 長さを秒で計算
        duration = frames / float(frame_rate)
    return duration

def extract_number(s):
    # 文字列から数値を抽出する正規表現
    match = int(s[s.rfind("\\")+1:s.find("_")])
    return match

# WAV ファイルの長さを取得

data=crete()

file_paths = glob.glob('on/*.wav')
print(file_paths)
num=0
file_paths.sort(key=extract_number)
print(file_paths)
for pas in file_paths:
    long=int(get_wav_duration(pas)*32)+2
    sr=pas[pas.rfind('_')+1:pas.find('.')]
    mat=pas[pas.find('_')+1:pas.rfind('_')]
    data["Timeline"]["Items"].append(crete_audio(pas,length=long,frame=num))
    data["Timeline"]["Items"].append(crete_Text(sr,length=long,frame=num))
    num+=long

with open("project.ymmp", "w") as json_file:
    json.dump(data, json_file,indent=4)
