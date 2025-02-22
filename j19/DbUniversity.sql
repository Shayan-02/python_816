USE DbUniversity
GO
/****** Object:  Table [dbo].[TblCourse]    Script Date: 11/28/2023 8:33:38 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TblCourse](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[CoID] [int] NOT NULL,
	[Cotitle] [nvarchar](50) NOT NULL,
	[Credit] [bigint] NOT NULL,
	[Type] [nvarchar](50) NOT NULL,
	[Date] [nvarchar](50) NULL,
 CONSTRAINT [PK_TblCourse] PRIMARY KEY CLUSTERED 
(
	[CoID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TblStCo]    Script Date: 11/28/2023 8:33:39 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TblStCo](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[StId] [bigint] NOT NULL,
	[CoID] [int] NOT NULL,
	[TeacherID] [int] NOT NULL,
	[Year] [varchar](9) NOT NULL,
	[Term] [tinyint] NOT NULL,
	[Grade] [decimal](4, 2) NOT NULL,
 CONSTRAINT [PK_TblStCo_1] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TblStudent]    Script Date: 11/28/2023 8:33:39 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TblStudent](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Stid] [bigint] NOT NULL,
	[StName] [nvarchar](50) NOT NULL,
	[Major] [nvarchar](50) NOT NULL,
	[Degree] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_TblStudent] PRIMARY KEY CLUSTERED 
(
	[Stid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TEACHER]    Script Date: 11/28/2023 8:33:39 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TEACHER](
	[TeachId] [int] NOT NULL,
	[TeachName] [nvarchar](21) NOT NULL,
	[Tel] [varchar](21) NULL,
PRIMARY KEY CLUSTERED 
(
	[TeachId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[TblCourse] ON 

INSERT [dbo].[TblCourse] ([ID], [CoID], [Cotitle], [Credit], [Type], [Date]) VALUES (11, 1001, N'پایگاه داده', 3, N'نظری', N'پنجنشبه')
INSERT [dbo].[TblCourse] ([ID], [CoID], [Cotitle], [Credit], [Type], [Date]) VALUES (12, 1002, N'آزمایشگاه پایگاه داده', 1, N'عملی', N'جمعه')
INSERT [dbo].[TblCourse] ([ID], [CoID], [Cotitle], [Credit], [Type], [Date]) VALUES (13, 1003, N'معماری کامپیوتر', 2, N'نظری', N'دوشنبه')
INSERT [dbo].[TblCourse] ([ID], [CoID], [Cotitle], [Credit], [Type], [Date]) VALUES (14, 1004, N'آزمایشگاه معماری کامپیوتر', 1, N'عملی', N'سه شنبه')
INSERT [dbo].[TblCourse] ([ID], [CoID], [Cotitle], [Credit], [Type], [Date]) VALUES (9, 2001, N'شیمی', 3, N'نظری', N'یکشنبه')
INSERT [dbo].[TblCourse] ([ID], [CoID], [Cotitle], [Credit], [Type], [Date]) VALUES (10, 2002, N'آزمایشگاه شیمی', 1, N'عملی', N'یکشنبه')
SET IDENTITY_INSERT [dbo].[TblCourse] OFF
GO
SET IDENTITY_INSERT [dbo].[TblStCo] ON 

INSERT [dbo].[TblStCo] ([ID], [StId], [CoID], [TeacherID], [Year], [Term], [Grade]) VALUES (2, 4000304, 1001, 40001, N'1400', 1, CAST(19.00 AS Decimal(4, 2)))
INSERT [dbo].[TblStCo] ([ID], [StId], [CoID], [TeacherID], [Year], [Term], [Grade]) VALUES (3, 9713843, 2001, 40002, N'1400', 1, CAST(12.00 AS Decimal(4, 2)))
INSERT [dbo].[TblStCo] ([ID], [StId], [CoID], [TeacherID], [Year], [Term], [Grade]) VALUES (4, 4002030, 2002, 40003, N'1400', 2, CAST(20.00 AS Decimal(4, 2)))
INSERT [dbo].[TblStCo] ([ID], [StId], [CoID], [TeacherID], [Year], [Term], [Grade]) VALUES (6, 4002030, 2001, 40001, N'1401', 1, CAST(17.00 AS Decimal(4, 2)))
SET IDENTITY_INSERT [dbo].[TblStCo] OFF
GO
SET IDENTITY_INSERT [dbo].[TblStudent] ON 

INSERT [dbo].[TblStudent] ([ID], [Stid], [StName], [Major], [Degree]) VALUES (16, 323223, N'محمد سلیمی', N'کامپیوتر', N'کارشناسی')
INSERT [dbo].[TblStudent] ([ID], [Stid], [StName], [Major], [Degree]) VALUES (15, 4000304, N'زهرا قلی زاده', N'کامپیوتر', N'کارشناسی')
INSERT [dbo].[TblStudent] ([ID], [Stid], [StName], [Major], [Degree]) VALUES (11, 4000321, N'فاطمه رمضانی', N'کامپیوتر', N'کارشناسی')
INSERT [dbo].[TblStudent] ([ID], [Stid], [StName], [Major], [Degree]) VALUES (8, 4002030, N'رضا سعیدی', N'کامپیوتر', N'کارشناسی')
INSERT [dbo].[TblStudent] ([ID], [Stid], [StName], [Major], [Degree]) VALUES (4, 9713843, N'رضا طاهری', N'شیمی', N'کارشناسی')
INSERT [dbo].[TblStudent] ([ID], [Stid], [StName], [Major], [Degree]) VALUES (10, 9830403, N'محمد محمدی', N'کامپیوتر', N'کارشناسی')
INSERT [dbo].[TblStudent] ([ID], [Stid], [StName], [Major], [Degree]) VALUES (7, 9932932, N'سعید محمودی', N'کامپیوتر', N'کارشناسی ارشد')
SET IDENTITY_INSERT [dbo].[TblStudent] OFF
GO
INSERT [dbo].[TEACHER] ([TeachId], [TeachName], [Tel]) VALUES (4004, N'محمد روشن پناه', N'3232')
INSERT [dbo].[TEACHER] ([TeachId], [TeachName], [Tel]) VALUES (40000, N'وحید غلامی', N'49340493')
INSERT [dbo].[TEACHER] ([TeachId], [TeachName], [Tel]) VALUES (40001, N'حسین رضایی', N'40303032')
INSERT [dbo].[TEACHER] ([TeachId], [TeachName], [Tel]) VALUES (40002, N'سعید رضا زاده', N'3001002')
INSERT [dbo].[TEACHER] ([TeachId], [TeachName], [Tel]) VALUES (40003, N'علی صیادی', N'3020023')
GO
ALTER TABLE [dbo].[TblStudent] ADD  DEFAULT (N'کاردانی') FOR [Degree]
GO
ALTER TABLE [dbo].[TblStCo]  WITH CHECK ADD  CONSTRAINT [FK_TblStCo_TblCourse] FOREIGN KEY([CoID])
REFERENCES [dbo].[TblCourse] ([CoID])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[TblStCo] CHECK CONSTRAINT [FK_TblStCo_TblCourse]
GO
ALTER TABLE [dbo].[TblStCo]  WITH CHECK ADD  CONSTRAINT [FK_TblStCo_TblStudent] FOREIGN KEY([StId])
REFERENCES [dbo].[TblStudent] ([Stid])
GO
ALTER TABLE [dbo].[TblStCo] CHECK CONSTRAINT [FK_TblStCo_TblStudent]
GO
ALTER TABLE [dbo].[TblStCo]  WITH CHECK ADD  CONSTRAINT [FK_TblStCo_TEACHER] FOREIGN KEY([TeacherID])
REFERENCES [dbo].[TEACHER] ([TeachId])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[TblStCo] CHECK CONSTRAINT [FK_TblStCo_TEACHER]
GO
