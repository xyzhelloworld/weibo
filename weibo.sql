CREATE DATABASE weibo DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE TABLE PersonInfo
(
    UserId varchar(10) primary key,
    Nickname varchar(20), 
    Sex varchar(2),
    Region varchar(64)
)default charset=utf8;

CREATE TABLE Weibo
(
    WeiboHash varchar(16) primary key comment "微博hash值",
    UserId varchar(10),
    Weibo varchar(300),
    Comments int(32) comment "微博评论数",
    Forwardings int(32) comment "微博转发数",
    Thumb int(32) comment "微博赞数",
    foreign key(UserId) references PersonInfo(UserId) on delete cascade on update cascade
)default charset=utf8;

CREATE TABLE Education
(
    UserId varchar(10),
    School varchar(20), 
    `Bagin` varchar(4),
    foreign key(UserId) references PersonInfo(UserId) on delete cascade on update cascade
)default charset=utf8;

CREATE TABLE Job
(
    UserId varchar(10),
    Company varchar(20), 
    `Bagin` varchar(4),
    `End` varchar(4),
    foreign key(UserId) references PersonInfo(UserId) on delete cascade on update cascade
)default charset=utf8;

CREATE TABLE InterestTag
(
    UserId varchar(10),
    Tag varchar(20), 
    foreign key(UserId) references PersonInfo(UserId) on delete cascade on update cascade
)default charset=utf8;