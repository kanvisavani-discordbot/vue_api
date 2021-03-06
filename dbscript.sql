USE [bt_interviews]
GO
/****** Object:  Table [dbo].[tbl_users]    Script Date: 10/2/2021 10:24:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_users](
	[id] [varchar](36) NOT NULL,
	[user_name] [varchar](50) NULL,
	[profile_pic] [varchar](50) NULL,
 CONSTRAINT [PK_tbl_userEvents] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[tbl_users] ADD  CONSTRAINT [DF_tbl_userEvents_id]  DEFAULT (newid()) FOR [id]
GO
