from dataclasses import dataclass


@dataclass
class MessageContent:
    html: str
    markdown: str


@dataclass
class File:
    name: str
    url: str


@dataclass
class Message:
    id: str
    visits: int
    ctime: str
    utime: str
    keywords: list[str]
    announcer: str
    title: str
    content: MessageContent
    files: list[File]


@dataclass
class Classified:
    id: str
    name: str
    module_id: str
    section_id: str
    rss: str
    messages: list[Message]
