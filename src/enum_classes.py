from enum import Enum

class TabCreatorState(Enum):
    IDLE = 1
    DEFINING_TEMPO = 2
    DEFINING_BEATS = 3

class SessionRecorderState(Enum):
    IDLE= 1
    METRONOME_ON = 2
    ARMED = 3
    RECORDING = 4
    SAVING = 5
    PLAYER_IDLE = 6
    PLAYER_SELECTION_START = 7
    PLAYER_SELECTION_END = 8
    PLAYER_ON = 9