from enum import Enum

"""From API endpoints
we have these strings which  can be converted into URL strings or they
fail because not in the Class MessageType
"""


class MessageType(Enum):
    CHAT_ENDED_EVENT = "chatEndedEvent"
    MESSAGE_DELETED_EVENT = "messageDeletedEvent"
    NEW_SPONSOR_EVENT = "newSponsorEvent"
    SPONSOR_ONLY_MODE_ENDED_EVENT = "sponsorOnlyModeEndedEvent"
    SPONSOR_ONLY_MODE_STARTED_EVENT = "sponsorOnlyModeStartedEvent"
    MEMBER_MILESTONE_CHAT_EVENT = "memberMilestoneChat Event"
    SUPER_CHAT_EVENT = "superChatEvent"
    SUPER_STICKER_EVENT = "superStickerEvent"
    TEXT_MESSAGE_EVENT = "textMessageEvent"
    TOMBSTONE = "tombstone"
    USER_BANNED_EVENT = "userBannedEvent"


value = "chatEndedEvent"
print(MessageType(value))
print(MessageType(value).name)

print(MessageType.SUPER_CHAT_EVENT)
print(type(MessageType.SUPER_CHAT_EVENT))

print(MessageType.SUPER_CHAT_EVENT.value)
print(type(MessageType.SUPER_CHAT_EVENT.value))

print(MessageType.SUPER_CHAT_EVENT.name)
print(type(MessageType.SUPER_CHAT_EVENT.name))