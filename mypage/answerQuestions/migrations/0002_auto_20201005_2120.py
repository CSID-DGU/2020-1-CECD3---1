# Generated by Django 3.1 on 2020-10-05 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answerQuestions', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Assistant',
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.RemoveField(
            model_name='enroll',
            name='s',
        ),
        migrations.DeleteModel(
            name='MdlAnalyticsIndicatorCalc',
        ),
        migrations.DeleteModel(
            name='MdlAnalyticsModels',
        ),
        migrations.DeleteModel(
            name='MdlAnalyticsModelsLog',
        ),
        migrations.DeleteModel(
            name='MdlAnalyticsPredictionActions',
        ),
        migrations.DeleteModel(
            name='MdlAnalyticsPredictions',
        ),
        migrations.DeleteModel(
            name='MdlAnalyticsPredictSamples',
        ),
        migrations.DeleteModel(
            name='MdlAnalyticsTrainSamples',
        ),
        migrations.DeleteModel(
            name='MdlAnalyticsUsedAnalysables',
        ),
        migrations.DeleteModel(
            name='MdlAnalyticsUsedFiles',
        ),
        migrations.DeleteModel(
            name='MdlAssign',
        ),
        migrations.DeleteModel(
            name='MdlAssignfeedbackComments',
        ),
        migrations.DeleteModel(
            name='MdlAssignfeedbackEditpdfAnnot',
        ),
        migrations.DeleteModel(
            name='MdlAssignfeedbackEditpdfCmnt',
        ),
        migrations.DeleteModel(
            name='MdlAssignfeedbackEditpdfQueue',
        ),
        migrations.DeleteModel(
            name='MdlAssignfeedbackEditpdfQuick',
        ),
        migrations.DeleteModel(
            name='MdlAssignfeedbackEditpdfRot',
        ),
        migrations.DeleteModel(
            name='MdlAssignfeedbackFile',
        ),
        migrations.DeleteModel(
            name='MdlAssignGrades',
        ),
        migrations.DeleteModel(
            name='MdlAssignment',
        ),
        migrations.DeleteModel(
            name='MdlAssignmentSubmissions',
        ),
        migrations.DeleteModel(
            name='MdlAssignmentUpgrade',
        ),
        migrations.DeleteModel(
            name='MdlAssignOverrides',
        ),
        migrations.DeleteModel(
            name='MdlAssignPluginConfig',
        ),
        migrations.DeleteModel(
            name='MdlAssignSubmission',
        ),
        migrations.DeleteModel(
            name='MdlAssignsubmissionFile',
        ),
        migrations.DeleteModel(
            name='MdlAssignsubmissionOnlinetext',
        ),
        migrations.DeleteModel(
            name='MdlAssignUserFlags',
        ),
        migrations.DeleteModel(
            name='MdlAssignUserMapping',
        ),
        migrations.DeleteModel(
            name='MdlAuthOauth2LinkedLogin',
        ),
        migrations.DeleteModel(
            name='MdlBackupControllers',
        ),
        migrations.DeleteModel(
            name='MdlBackupCourses',
        ),
        migrations.DeleteModel(
            name='MdlBackupLogs',
        ),
        migrations.DeleteModel(
            name='MdlBadge',
        ),
        migrations.DeleteModel(
            name='MdlBadgeAlignment',
        ),
        migrations.DeleteModel(
            name='MdlBadgeBackpack',
        ),
        migrations.DeleteModel(
            name='MdlBadgeBackpackOauth2',
        ),
        migrations.DeleteModel(
            name='MdlBadgeCriteria',
        ),
        migrations.DeleteModel(
            name='MdlBadgeCriteriaMet',
        ),
        migrations.DeleteModel(
            name='MdlBadgeCriteriaParam',
        ),
        migrations.DeleteModel(
            name='MdlBadgeEndorsement',
        ),
        migrations.DeleteModel(
            name='MdlBadgeExternal',
        ),
        migrations.DeleteModel(
            name='MdlBadgeExternalBackpack',
        ),
        migrations.DeleteModel(
            name='MdlBadgeExternalIdentifier',
        ),
        migrations.DeleteModel(
            name='MdlBadgeIssued',
        ),
        migrations.DeleteModel(
            name='MdlBadgeManualAward',
        ),
        migrations.DeleteModel(
            name='MdlBadgeRelated',
        ),
        migrations.DeleteModel(
            name='MdlBlock',
        ),
        migrations.DeleteModel(
            name='MdlBlockInstances',
        ),
        migrations.DeleteModel(
            name='MdlBlockPositions',
        ),
        migrations.DeleteModel(
            name='MdlBlockRecentActivity',
        ),
        migrations.DeleteModel(
            name='MdlBlockRecentlyaccesseditems',
        ),
        migrations.DeleteModel(
            name='MdlBlockRssClient',
        ),
        migrations.DeleteModel(
            name='MdlBlogAssociation',
        ),
        migrations.DeleteModel(
            name='MdlBlogExternal',
        ),
        migrations.DeleteModel(
            name='MdlBook',
        ),
        migrations.DeleteModel(
            name='MdlBookChapters',
        ),
        migrations.DeleteModel(
            name='MdlCacheFilters',
        ),
        migrations.DeleteModel(
            name='MdlCacheFlags',
        ),
        migrations.DeleteModel(
            name='MdlCapabilities',
        ),
        migrations.DeleteModel(
            name='MdlChat',
        ),
        migrations.DeleteModel(
            name='MdlChatMessages',
        ),
        migrations.DeleteModel(
            name='MdlChatMessagesCurrent',
        ),
        migrations.DeleteModel(
            name='MdlChatUsers',
        ),
        migrations.DeleteModel(
            name='MdlChoice',
        ),
        migrations.DeleteModel(
            name='MdlChoiceAnswers',
        ),
        migrations.DeleteModel(
            name='MdlChoiceOptions',
        ),
        migrations.DeleteModel(
            name='MdlCohort',
        ),
        migrations.DeleteModel(
            name='MdlCohortMembers',
        ),
        migrations.DeleteModel(
            name='MdlComments',
        ),
        migrations.DeleteModel(
            name='MdlCompetency',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyCoursecomp',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyCoursecompsetting',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyEvidence',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyFramework',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyModulecomp',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyPlan',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyPlancomp',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyRelatedcomp',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyTemplate',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyTemplatecohort',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyTemplatecomp',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyUsercomp',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyUsercompcourse',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyUsercompplan',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyUserevidence',
        ),
        migrations.DeleteModel(
            name='MdlCompetencyUserevidencecomp',
        ),
        migrations.DeleteModel(
            name='MdlConfig',
        ),
        migrations.DeleteModel(
            name='MdlConfigLog',
        ),
        migrations.DeleteModel(
            name='MdlConfigPlugins',
        ),
        migrations.DeleteModel(
            name='MdlContentbankContent',
        ),
        migrations.DeleteModel(
            name='MdlContext',
        ),
        migrations.DeleteModel(
            name='MdlContextTemp',
        ),
        migrations.DeleteModel(
            name='MdlCourse',
        ),
        migrations.DeleteModel(
            name='MdlCourseCategories',
        ),
        migrations.DeleteModel(
            name='MdlCourseCompletionAggrMethd',
        ),
        migrations.DeleteModel(
            name='MdlCourseCompletionCritCompl',
        ),
        migrations.DeleteModel(
            name='MdlCourseCompletionCriteria',
        ),
        migrations.DeleteModel(
            name='MdlCourseCompletionDefaults',
        ),
        migrations.DeleteModel(
            name='MdlCourseCompletions',
        ),
        migrations.DeleteModel(
            name='MdlCourseFormatOptions',
        ),
        migrations.DeleteModel(
            name='MdlCourseModules',
        ),
        migrations.DeleteModel(
            name='MdlCourseModulesCompletion',
        ),
        migrations.DeleteModel(
            name='MdlCoursePublished',
        ),
        migrations.DeleteModel(
            name='MdlCourseRequest',
        ),
        migrations.DeleteModel(
            name='MdlCourseSections',
        ),
        migrations.DeleteModel(
            name='MdlCustomfieldCategory',
        ),
        migrations.DeleteModel(
            name='MdlCustomfieldData',
        ),
        migrations.DeleteModel(
            name='MdlCustomfieldField',
        ),
        migrations.DeleteModel(
            name='MdlData',
        ),
        migrations.DeleteModel(
            name='MdlDataContent',
        ),
        migrations.DeleteModel(
            name='MdlDataFields',
        ),
        migrations.DeleteModel(
            name='MdlDataRecords',
        ),
        migrations.DeleteModel(
            name='MdlEditorAttoAutosave',
        ),
        migrations.DeleteModel(
            name='MdlEnrol',
        ),
        migrations.DeleteModel(
            name='MdlEnrolLtiLti2Consumer',
        ),
        migrations.DeleteModel(
            name='MdlEnrolLtiLti2Context',
        ),
        migrations.DeleteModel(
            name='MdlEnrolLtiLti2Nonce',
        ),
        migrations.DeleteModel(
            name='MdlEnrolLtiLti2ResourceLink',
        ),
        migrations.DeleteModel(
            name='MdlEnrolLtiLti2ShareKey',
        ),
        migrations.DeleteModel(
            name='MdlEnrolLtiLti2ToolProxy',
        ),
        migrations.DeleteModel(
            name='MdlEnrolLtiLti2UserResult',
        ),
        migrations.DeleteModel(
            name='MdlEnrolLtiToolConsumerMap',
        ),
        migrations.DeleteModel(
            name='MdlEnrolLtiTools',
        ),
        migrations.DeleteModel(
            name='MdlEnrolLtiUsers',
        ),
        migrations.DeleteModel(
            name='MdlEnrolPaypal',
        ),
        migrations.DeleteModel(
            name='MdlEvent',
        ),
        migrations.DeleteModel(
            name='MdlEventsHandlers',
        ),
        migrations.DeleteModel(
            name='MdlEventsQueue',
        ),
        migrations.DeleteModel(
            name='MdlEventsQueueHandlers',
        ),
        migrations.DeleteModel(
            name='MdlEventSubscriptions',
        ),
        migrations.DeleteModel(
            name='MdlExternalFunctions',
        ),
        migrations.DeleteModel(
            name='MdlExternalServices',
        ),
        migrations.DeleteModel(
            name='MdlExternalServicesFunctions',
        ),
        migrations.DeleteModel(
            name='MdlExternalServicesUsers',
        ),
        migrations.DeleteModel(
            name='MdlExternalTokens',
        ),
        migrations.DeleteModel(
            name='MdlFavourite',
        ),
        migrations.DeleteModel(
            name='MdlFeedback',
        ),
        migrations.DeleteModel(
            name='MdlFeedbackCompleted',
        ),
        migrations.DeleteModel(
            name='MdlFeedbackCompletedtmp',
        ),
        migrations.DeleteModel(
            name='MdlFeedbackItem',
        ),
        migrations.DeleteModel(
            name='MdlFeedbackSitecourseMap',
        ),
        migrations.DeleteModel(
            name='MdlFeedbackTemplate',
        ),
        migrations.DeleteModel(
            name='MdlFeedbackValue',
        ),
        migrations.DeleteModel(
            name='MdlFeedbackValuetmp',
        ),
        migrations.DeleteModel(
            name='MdlFileConversion',
        ),
        migrations.DeleteModel(
            name='MdlFiles',
        ),
        migrations.DeleteModel(
            name='MdlFilesReference',
        ),
        migrations.DeleteModel(
            name='MdlFilterActive',
        ),
        migrations.DeleteModel(
            name='MdlFilterConfig',
        ),
        migrations.DeleteModel(
            name='MdlFolder',
        ),
        migrations.DeleteModel(
            name='MdlForum',
        ),
        migrations.DeleteModel(
            name='MdlForumDigests',
        ),
        migrations.DeleteModel(
            name='MdlForumDiscussions',
        ),
        migrations.DeleteModel(
            name='MdlForumDiscussionSubs',
        ),
        migrations.DeleteModel(
            name='MdlForumGrades',
        ),
        migrations.DeleteModel(
            name='MdlForumPosts',
        ),
        migrations.DeleteModel(
            name='MdlForumQueue',
        ),
        migrations.DeleteModel(
            name='MdlForumRead',
        ),
        migrations.DeleteModel(
            name='MdlForumSubscriptions',
        ),
        migrations.DeleteModel(
            name='MdlForumTrackPrefs',
        ),
        migrations.DeleteModel(
            name='MdlGlossary',
        ),
        migrations.DeleteModel(
            name='MdlGlossaryAlias',
        ),
        migrations.DeleteModel(
            name='MdlGlossaryCategories',
        ),
        migrations.DeleteModel(
            name='MdlGlossaryEntries',
        ),
        migrations.DeleteModel(
            name='MdlGlossaryEntriesCategories',
        ),
        migrations.DeleteModel(
            name='MdlGlossaryFormats',
        ),
        migrations.DeleteModel(
            name='MdlGradeCategories',
        ),
        migrations.DeleteModel(
            name='MdlGradeCategoriesHistory',
        ),
        migrations.DeleteModel(
            name='MdlGradeGrades',
        ),
        migrations.DeleteModel(
            name='MdlGradeGradesHistory',
        ),
        migrations.DeleteModel(
            name='MdlGradeImportNewitem',
        ),
        migrations.DeleteModel(
            name='MdlGradeImportValues',
        ),
        migrations.DeleteModel(
            name='MdlGradeItems',
        ),
        migrations.DeleteModel(
            name='MdlGradeItemsHistory',
        ),
        migrations.DeleteModel(
            name='MdlGradeLetters',
        ),
        migrations.DeleteModel(
            name='MdlGradeOutcomes',
        ),
        migrations.DeleteModel(
            name='MdlGradeOutcomesCourses',
        ),
        migrations.DeleteModel(
            name='MdlGradeOutcomesHistory',
        ),
        migrations.DeleteModel(
            name='MdlGradeSettings',
        ),
        migrations.DeleteModel(
            name='MdlGradingAreas',
        ),
        migrations.DeleteModel(
            name='MdlGradingDefinitions',
        ),
        migrations.DeleteModel(
            name='MdlGradingformGuideComments',
        ),
        migrations.DeleteModel(
            name='MdlGradingformGuideCriteria',
        ),
        migrations.DeleteModel(
            name='MdlGradingformGuideFillings',
        ),
        migrations.DeleteModel(
            name='MdlGradingformRubricCriteria',
        ),
        migrations.DeleteModel(
            name='MdlGradingformRubricFillings',
        ),
        migrations.DeleteModel(
            name='MdlGradingformRubricLevels',
        ),
        migrations.DeleteModel(
            name='MdlGradingInstances',
        ),
        migrations.DeleteModel(
            name='MdlGroupings',
        ),
        migrations.DeleteModel(
            name='MdlGroupingsGroups',
        ),
        migrations.DeleteModel(
            name='MdlGroups',
        ),
        migrations.DeleteModel(
            name='MdlGroupsMembers',
        ),
        migrations.DeleteModel(
            name='MdlH5P',
        ),
        migrations.DeleteModel(
            name='MdlH5Pactivity',
        ),
        migrations.DeleteModel(
            name='MdlH5PactivityAttempts',
        ),
        migrations.DeleteModel(
            name='MdlH5PactivityAttemptsResults',
        ),
        migrations.DeleteModel(
            name='MdlH5PContentsLibraries',
        ),
        migrations.DeleteModel(
            name='MdlH5PLibraries',
        ),
        migrations.DeleteModel(
            name='MdlH5PLibrariesCachedassets',
        ),
        migrations.DeleteModel(
            name='MdlH5PLibraryDependencies',
        ),
        migrations.DeleteModel(
            name='MdlImscp',
        ),
        migrations.DeleteModel(
            name='MdlLabel',
        ),
        migrations.DeleteModel(
            name='MdlLesson',
        ),
        migrations.DeleteModel(
            name='MdlLessonAnswers',
        ),
        migrations.DeleteModel(
            name='MdlLessonAttempts',
        ),
        migrations.DeleteModel(
            name='MdlLessonBranch',
        ),
        migrations.DeleteModel(
            name='MdlLessonGrades',
        ),
        migrations.DeleteModel(
            name='MdlLessonOverrides',
        ),
        migrations.DeleteModel(
            name='MdlLessonPages',
        ),
        migrations.DeleteModel(
            name='MdlLessonTimer',
        ),
        migrations.DeleteModel(
            name='MdlLicense',
        ),
        migrations.DeleteModel(
            name='MdlLockDb',
        ),
        migrations.DeleteModel(
            name='MdlLog',
        ),
        migrations.DeleteModel(
            name='MdlLogDisplay',
        ),
        migrations.DeleteModel(
            name='MdlLogQueries',
        ),
        migrations.DeleteModel(
            name='MdlLogstoreStandardLog',
        ),
        migrations.DeleteModel(
            name='MdlLti',
        ),
        migrations.DeleteModel(
            name='MdlLtiAccessTokens',
        ),
        migrations.DeleteModel(
            name='MdlLtiserviceGradebookservices',
        ),
        migrations.DeleteModel(
            name='MdlLtiSubmission',
        ),
        migrations.DeleteModel(
            name='MdlLtiToolProxies',
        ),
        migrations.DeleteModel(
            name='MdlLtiToolSettings',
        ),
        migrations.DeleteModel(
            name='MdlLtiTypes',
        ),
        migrations.DeleteModel(
            name='MdlLtiTypesConfig',
        ),
        migrations.DeleteModel(
            name='MdlMessage',
        ),
        migrations.DeleteModel(
            name='MdlMessageAirnotifierDevices',
        ),
        migrations.DeleteModel(
            name='MdlMessageContactRequests',
        ),
        migrations.DeleteModel(
            name='MdlMessageContacts',
        ),
        migrations.DeleteModel(
            name='MdlMessageConversationActions',
        ),
        migrations.DeleteModel(
            name='MdlMessageConversationMembers',
        ),
        migrations.DeleteModel(
            name='MdlMessageConversations',
        ),
        migrations.DeleteModel(
            name='MdlMessageEmailMessages',
        ),
        migrations.DeleteModel(
            name='MdlMessageinboundDatakeys',
        ),
        migrations.DeleteModel(
            name='MdlMessageinboundHandlers',
        ),
        migrations.DeleteModel(
            name='MdlMessageinboundMessagelist',
        ),
        migrations.DeleteModel(
            name='MdlMessagePopup',
        ),
        migrations.DeleteModel(
            name='MdlMessagePopupNotifications',
        ),
        migrations.DeleteModel(
            name='MdlMessageProcessors',
        ),
        migrations.DeleteModel(
            name='MdlMessageProviders',
        ),
        migrations.DeleteModel(
            name='MdlMessageRead',
        ),
        migrations.DeleteModel(
            name='MdlMessages',
        ),
        migrations.DeleteModel(
            name='MdlMessageUserActions',
        ),
        migrations.DeleteModel(
            name='MdlMessageUsersBlocked',
        ),
        migrations.DeleteModel(
            name='MdlMnetApplication',
        ),
        migrations.DeleteModel(
            name='MdlMnetHost',
        ),
        migrations.DeleteModel(
            name='MdlMnetHost2Service',
        ),
        migrations.DeleteModel(
            name='MdlMnetLog',
        ),
        migrations.DeleteModel(
            name='MdlMnetRemoteRpc',
        ),
        migrations.DeleteModel(
            name='MdlMnetRemoteService2Rpc',
        ),
        migrations.DeleteModel(
            name='MdlMnetRpc',
        ),
        migrations.DeleteModel(
            name='MdlMnetService',
        ),
        migrations.DeleteModel(
            name='MdlMnetService2Rpc',
        ),
        migrations.DeleteModel(
            name='MdlMnetserviceEnrolCourses',
        ),
        migrations.DeleteModel(
            name='MdlMnetserviceEnrolEnrolments',
        ),
        migrations.DeleteModel(
            name='MdlMnetSession',
        ),
        migrations.DeleteModel(
            name='MdlMnetSsoAccessControl',
        ),
        migrations.DeleteModel(
            name='MdlModules',
        ),
        migrations.DeleteModel(
            name='MdlMyPages',
        ),
        migrations.DeleteModel(
            name='MdlNotifications',
        ),
        migrations.DeleteModel(
            name='MdlOauth2AccessToken',
        ),
        migrations.DeleteModel(
            name='MdlOauth2Endpoint',
        ),
        migrations.DeleteModel(
            name='MdlOauth2Issuer',
        ),
        migrations.DeleteModel(
            name='MdlOauth2SystemAccount',
        ),
        migrations.DeleteModel(
            name='MdlOauth2UserFieldMapping',
        ),
        migrations.DeleteModel(
            name='MdlPage',
        ),
        migrations.DeleteModel(
            name='MdlPortfolioInstance',
        ),
        migrations.DeleteModel(
            name='MdlPortfolioInstanceConfig',
        ),
        migrations.DeleteModel(
            name='MdlPortfolioInstanceUser',
        ),
        migrations.DeleteModel(
            name='MdlPortfolioLog',
        ),
        migrations.DeleteModel(
            name='MdlPortfolioMaharaQueue',
        ),
        migrations.DeleteModel(
            name='MdlPortfolioTempdata',
        ),
        migrations.DeleteModel(
            name='MdlPost',
        ),
        migrations.DeleteModel(
            name='MdlProfiling',
        ),
        migrations.DeleteModel(
            name='MdlQtypeDdimageortext',
        ),
        migrations.DeleteModel(
            name='MdlQtypeDdimageortextDrags',
        ),
        migrations.DeleteModel(
            name='MdlQtypeDdimageortextDrops',
        ),
        migrations.DeleteModel(
            name='MdlQtypeDdmarker',
        ),
        migrations.DeleteModel(
            name='MdlQtypeDdmarkerDrags',
        ),
        migrations.DeleteModel(
            name='MdlQtypeDdmarkerDrops',
        ),
        migrations.DeleteModel(
            name='MdlQtypeEssayOptions',
        ),
        migrations.DeleteModel(
            name='MdlQtypeMatchOptions',
        ),
        migrations.DeleteModel(
            name='MdlQtypeMatchSubquestions',
        ),
        migrations.DeleteModel(
            name='MdlQtypeMultichoiceOptions',
        ),
        migrations.DeleteModel(
            name='MdlQtypeRandomsamatchOptions',
        ),
        migrations.DeleteModel(
            name='MdlQtypeShortanswerOptions',
        ),
        migrations.DeleteModel(
            name='MdlQuestion',
        ),
        migrations.DeleteModel(
            name='MdlQuestionAnswers',
        ),
        migrations.DeleteModel(
            name='MdlQuestionAttempts',
        ),
        migrations.DeleteModel(
            name='MdlQuestionAttemptStepData',
        ),
        migrations.DeleteModel(
            name='MdlQuestionAttemptSteps',
        ),
        migrations.DeleteModel(
            name='MdlQuestionCalculated',
        ),
        migrations.DeleteModel(
            name='MdlQuestionCalculatedOptions',
        ),
        migrations.DeleteModel(
            name='MdlQuestionCategories',
        ),
        migrations.DeleteModel(
            name='MdlQuestionDatasetDefinitions',
        ),
        migrations.DeleteModel(
            name='MdlQuestionDatasetItems',
        ),
        migrations.DeleteModel(
            name='MdlQuestionDatasets',
        ),
        migrations.DeleteModel(
            name='MdlQuestionDdwtos',
        ),
        migrations.DeleteModel(
            name='MdlQuestionGapselect',
        ),
        migrations.DeleteModel(
            name='MdlQuestionHints',
        ),
        migrations.DeleteModel(
            name='MdlQuestionMultianswer',
        ),
        migrations.DeleteModel(
            name='MdlQuestionNumerical',
        ),
        migrations.DeleteModel(
            name='MdlQuestionNumericalOptions',
        ),
        migrations.DeleteModel(
            name='MdlQuestionNumericalUnits',
        ),
        migrations.DeleteModel(
            name='MdlQuestionResponseAnalysis',
        ),
        migrations.DeleteModel(
            name='MdlQuestionResponseCount',
        ),
        migrations.DeleteModel(
            name='MdlQuestionStatistics',
        ),
        migrations.DeleteModel(
            name='MdlQuestionTruefalse',
        ),
        migrations.DeleteModel(
            name='MdlQuestionUsages',
        ),
        migrations.DeleteModel(
            name='MdlQuiz',
        ),
        migrations.DeleteModel(
            name='MdlQuizaccessSebQuizsettings',
        ),
        migrations.DeleteModel(
            name='MdlQuizaccessSebTemplate',
        ),
        migrations.DeleteModel(
            name='MdlQuizAttempts',
        ),
        migrations.DeleteModel(
            name='MdlQuizFeedback',
        ),
        migrations.DeleteModel(
            name='MdlQuizGrades',
        ),
        migrations.DeleteModel(
            name='MdlQuizOverrides',
        ),
        migrations.DeleteModel(
            name='MdlQuizOverviewRegrades',
        ),
        migrations.DeleteModel(
            name='MdlQuizReports',
        ),
        migrations.DeleteModel(
            name='MdlQuizSections',
        ),
        migrations.DeleteModel(
            name='MdlQuizSlots',
        ),
        migrations.DeleteModel(
            name='MdlQuizSlotTags',
        ),
        migrations.DeleteModel(
            name='MdlQuizStatistics',
        ),
        migrations.DeleteModel(
            name='MdlRating',
        ),
        migrations.DeleteModel(
            name='MdlRegistrationHubs',
        ),
        migrations.DeleteModel(
            name='MdlRepository',
        ),
        migrations.DeleteModel(
            name='MdlRepositoryInstanceConfig',
        ),
        migrations.DeleteModel(
            name='MdlRepositoryInstances',
        ),
        migrations.DeleteModel(
            name='MdlRepositoryOnedriveAccess',
        ),
        migrations.DeleteModel(
            name='MdlResource',
        ),
        migrations.DeleteModel(
            name='MdlResourceOld',
        ),
        migrations.DeleteModel(
            name='MdlRole',
        ),
        migrations.DeleteModel(
            name='MdlRoleAllowAssign',
        ),
        migrations.DeleteModel(
            name='MdlRoleAllowOverride',
        ),
        migrations.DeleteModel(
            name='MdlRoleAllowSwitch',
        ),
        migrations.DeleteModel(
            name='MdlRoleAllowView',
        ),
        migrations.DeleteModel(
            name='MdlRoleAssignments',
        ),
        migrations.DeleteModel(
            name='MdlRoleCapabilities',
        ),
        migrations.DeleteModel(
            name='MdlRoleContextLevels',
        ),
        migrations.DeleteModel(
            name='MdlRoleNames',
        ),
        migrations.DeleteModel(
            name='MdlScale',
        ),
        migrations.DeleteModel(
            name='MdlScaleHistory',
        ),
        migrations.DeleteModel(
            name='MdlScorm',
        ),
        migrations.DeleteModel(
            name='MdlScormAiccSession',
        ),
        migrations.DeleteModel(
            name='MdlScormScoes',
        ),
        migrations.DeleteModel(
            name='MdlScormScoesData',
        ),
        migrations.DeleteModel(
            name='MdlScormScoesTrack',
        ),
        migrations.DeleteModel(
            name='MdlScormSeqMapinfo',
        ),
        migrations.DeleteModel(
            name='MdlScormSeqObjective',
        ),
        migrations.DeleteModel(
            name='MdlScormSeqRolluprule',
        ),
        migrations.DeleteModel(
            name='MdlScormSeqRolluprulecond',
        ),
        migrations.DeleteModel(
            name='MdlScormSeqRulecond',
        ),
        migrations.DeleteModel(
            name='MdlScormSeqRuleconds',
        ),
        migrations.DeleteModel(
            name='MdlSearchIndexRequests',
        ),
        migrations.DeleteModel(
            name='MdlSearchSimpledbIndex',
        ),
        migrations.DeleteModel(
            name='MdlSessions',
        ),
        migrations.DeleteModel(
            name='MdlStatsDaily',
        ),
        migrations.DeleteModel(
            name='MdlStatsMonthly',
        ),
        migrations.DeleteModel(
            name='MdlStatsUserDaily',
        ),
        migrations.DeleteModel(
            name='MdlStatsUserMonthly',
        ),
        migrations.DeleteModel(
            name='MdlStatsUserWeekly',
        ),
        migrations.DeleteModel(
            name='MdlStatsWeekly',
        ),
        migrations.DeleteModel(
            name='MdlSurvey',
        ),
        migrations.DeleteModel(
            name='MdlSurveyAnalysis',
        ),
        migrations.DeleteModel(
            name='MdlSurveyAnswers',
        ),
        migrations.DeleteModel(
            name='MdlSurveyQuestions',
        ),
        migrations.DeleteModel(
            name='MdlTag',
        ),
        migrations.DeleteModel(
            name='MdlTagArea',
        ),
        migrations.DeleteModel(
            name='MdlTagColl',
        ),
        migrations.DeleteModel(
            name='MdlTagCorrelation',
        ),
        migrations.DeleteModel(
            name='MdlTagInstance',
        ),
        migrations.DeleteModel(
            name='MdlTaskAdhoc',
        ),
        migrations.DeleteModel(
            name='MdlTaskLog',
        ),
        migrations.DeleteModel(
            name='MdlTaskScheduled',
        ),
        migrations.DeleteModel(
            name='MdlToolCohortroles',
        ),
        migrations.DeleteModel(
            name='MdlToolCustomlang',
        ),
        migrations.DeleteModel(
            name='MdlToolCustomlangComponents',
        ),
        migrations.DeleteModel(
            name='MdlToolDataprivacyCategory',
        ),
        migrations.DeleteModel(
            name='MdlToolDataprivacyCtxexpired',
        ),
        migrations.DeleteModel(
            name='MdlToolDataprivacyCtxinstance',
        ),
        migrations.DeleteModel(
            name='MdlToolDataprivacyCtxlevel',
        ),
        migrations.DeleteModel(
            name='MdlToolDataprivacyPurpose',
        ),
        migrations.DeleteModel(
            name='MdlToolDataprivacyPurposerole',
        ),
        migrations.DeleteModel(
            name='MdlToolDataprivacyRequest',
        ),
        migrations.DeleteModel(
            name='MdlToolMonitorEvents',
        ),
        migrations.DeleteModel(
            name='MdlToolMonitorHistory',
        ),
        migrations.DeleteModel(
            name='MdlToolMonitorRules',
        ),
        migrations.DeleteModel(
            name='MdlToolMonitorSubscriptions',
        ),
        migrations.DeleteModel(
            name='MdlToolPolicy',
        ),
        migrations.DeleteModel(
            name='MdlToolPolicyAcceptances',
        ),
        migrations.DeleteModel(
            name='MdlToolPolicyVersions',
        ),
        migrations.DeleteModel(
            name='MdlToolRecyclebinCategory',
        ),
        migrations.DeleteModel(
            name='MdlToolRecyclebinCourse',
        ),
        migrations.DeleteModel(
            name='MdlToolUsertoursSteps',
        ),
        migrations.DeleteModel(
            name='MdlToolUsertoursTours',
        ),
        migrations.DeleteModel(
            name='MdlUpgradeLog',
        ),
        migrations.DeleteModel(
            name='MdlUrl',
        ),
        migrations.DeleteModel(
            name='MdlUser',
        ),
        migrations.DeleteModel(
            name='MdlUserDevices',
        ),
        migrations.DeleteModel(
            name='MdlUserEnrolments',
        ),
        migrations.DeleteModel(
            name='MdlUserInfoCategory',
        ),
        migrations.DeleteModel(
            name='MdlUserInfoData',
        ),
        migrations.DeleteModel(
            name='MdlUserInfoField',
        ),
        migrations.DeleteModel(
            name='MdlUserLastaccess',
        ),
        migrations.DeleteModel(
            name='MdlUserPasswordHistory',
        ),
        migrations.DeleteModel(
            name='MdlUserPasswordResets',
        ),
        migrations.DeleteModel(
            name='MdlUserPreferences',
        ),
        migrations.DeleteModel(
            name='MdlUserPrivateKey',
        ),
        migrations.DeleteModel(
            name='MdlWiki',
        ),
        migrations.DeleteModel(
            name='MdlWikiLinks',
        ),
        migrations.DeleteModel(
            name='MdlWikiLocks',
        ),
        migrations.DeleteModel(
            name='MdlWikiPages',
        ),
        migrations.DeleteModel(
            name='MdlWikiSubwikis',
        ),
        migrations.DeleteModel(
            name='MdlWikiSynonyms',
        ),
        migrations.DeleteModel(
            name='MdlWikiVersions',
        ),
        migrations.DeleteModel(
            name='MdlWorkshop',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopAggregations',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopallocationScheduled',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopAssessments',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopevalBestSettings',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopformAccumulative',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopformComments',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopformNumerrors',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopformNumerrorsMap',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopformRubric',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopformRubricConfig',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopformRubricLevels',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopGrades',
        ),
        migrations.DeleteModel(
            name='MdlWorkshopSubmissions',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.DeleteModel(
            name='Teach',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='Enroll',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
