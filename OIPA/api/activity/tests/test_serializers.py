import pytest
from django.test import RequestFactory
from iati.factory import iati_factory
from api.activity import serializers


class TestActivitySerializers:

    request_dummy = RequestFactory().get('/')

    def test_DefaultAidTypeSerializer(self):
        aidtype = iati_factory.AidTypeFactory.build(
            code=10,
        )
        serializer = serializers.DefaultAidTypeSerializer(aidtype)
        assert serializer.data['code'] == str(aidtype.code), \
            """
            the data in aidtype.code should be serialized to a field named code
            inside the serialized object
            """

    def test_DefaultFlowTypeSerializer(self):
        flowtype = iati_factory.FlowTypeFactory.build(
            code=10,
        )
        serializer = serializers.DefaultFlowTypeSerializer(flowtype)
        assert serializer.data['code'] == flowtype.code, \
            """
            the data in flowtype.code should be serializer to a field named
            code inside the serialized object
            """

    def test_ActivityStatusSerializer(self):
        activity_status = iati_factory.ActivityStatusFactory.build(
            code=10,
        )
        serializer = serializers.ActivityStatusSerializer(activity_status)
        assert serializer.data['code'] == activity_status.code, \
            """
            the data in activity_status.code should be serialized to a field
            named code inside the serialized object
            """

    def test_CollaborationTypeSerializer(self):
        collaboration_type = iati_factory.CollaborationTypeFactory.build(
            code=1,
        )
        serializer = serializers.CollaborationTypeSerializer(
            collaboration_type)
        assert serializer.data['code'] == collaboration_type.code, \
            """
            the data in collaboration_type.code should be serialized to a field
            named code inside the serialized object
            """

    def test_TotalBudgetSerializer(self):
        activity = iati_factory.ActivityFactory.build(
            total_budget=1000,
            total_budget_currency=iati_factory.CurrencyFactory.build(
                code='USD')
        )
        serializer = serializers.TotalBudgetSerializer(activity)
        assert serializer.data['value'] == str(activity.total_budget), \
            """
            activity.total_budget should be serialized to a field called value
            inside the serialized object
            """
        assert 'currency' in serializer.data,\
            """
            a serialized total_budget object should contain a field called
            'currency'
            """

    def test_BudgetSerializer(self):
        budget = iati_factory.BudgetFactory.build(
            type_id=1,
            period_start='2014-12-1',
            period_end='2014-12-2',
        )
        serializer = serializers.BudgetSerializer(budget)
        assert serializer.data['type'] == budget.type_id, \
            """
            budget.type_id should be serialized to a field called 'type' inside
            the serializer object
            """
        assert serializer.data['period_start'] == budget.period_start, \
            """
            budget.period_start should be serialized to a field called
            period_start in the serialized object
            """
        assert serializer.data['period_end'] == budget.period_end, \
            """
            budget.period_end should be serialized to a field called
            period_end in the serialized object
            """
        assert 'value' in serializer.data, \
            """
            a serialized budget should contain an object called value
            """

    def test_ValueSerializer(self):
        budget = iati_factory.BudgetFactory.build(
            value=100,
            value_date='2014-12-1',
            currency=iati_factory.CurrencyFactory.build(code='USD')
        )
        serializer = serializers.BudgetSerializer.ValueSerializer(budget)
        assert serializer.data['value'] == str(budget.value), \
            """
            budget.value should be serialized to a field called value
            by the ValueSerializer
            """
        assert serializer.data['date'] == budget.value_date, \
            """
            budget.value_date should be serialized to  field called
            date by the ValueSerialized
            """
        assert 'currency' in serializer.data,\
            """
            a serialized value should contain an object valled 'currency'
            """

    def test_ActivityDateSerializer(self):
        activity = iati_factory.ActivityFactory.build(
            start_planned='2014-12-1',
            end_planned='2014-12-2',
            start_actual='2014-12-3',
            end_actual='2014-12-4',
        )
        serializer = serializers.ActivityDateSerializer(activity)
        assert serializer.data['start_planned'] == '2014-12-1', \
            """
            activity.start_planned should be serialized to a field called
            start_planned by the ActivityDateSerializer
            """
        assert serializer.data['end_planned'] == '2014-12-2', \
            """
            activity.end_planned should be serialized to a field called
            end_planned by the ActivityDateSerializer
            """
        assert serializer.data['start_actual'] == '2014-12-3', \
            """
            activity.start_actual should be serialized to a field called
            start_actual by the ActivityDateSerializer
            """
        assert serializer.data['end_actual'] == '2014-12-4', \
            """
            activity.end_actual should be serialized to a field called
            end_actual by the ActivityDateSerializer
            """

    @pytest.mark.django_db
    def test_ReportingOrganisationSerializer(self):
        organisation = iati_factory.OrganisationFactory.build()
        activity = iati_factory.ActivityFactory.build(
            secondary_publisher=True,
            reporting_organisation=organisation,
        )
        data = serializers.ReportingOrganisationSerializer(
            activity,
            context={'request': self.request_dummy}
        ).data
        assert data['secondary_reporter'] == activity.secondary_publisher,\
            """
            activity.secondary_publisher should be serialized to a field
            called 'secondary_reporter' by the ReportingOrganisationSerializer
            """
        assert 'organisation' in data, \
            """
            serializer.data should contain an object called 'organisation'
            """
        assert 'code' and 'name' and 'type' in data['organisation'], \
            """
            The organisation serialized by the ReportingOrganisationSerializer
            should atleast contain the fields 'code', 'name', and 'type'
            """

    def test_ActivityPolicyMarkerSerializer(self):
        policy_marker = iati_factory.ActivityPolicyMarkerFactory.build(
            alt_policy_marker='alt_policy_marker',
        )
        data = serializers.ActivityPolicyMarkerSerializer(policy_marker).data
        assert data['narative'] == policy_marker.alt_policy_marker,\
            """
            policy_marker.alt_policy_marker should be serialized to a field
            called 'narative'
            """
        assert 'vocabulary' in data,\
            'serializer.data should contain an object called vocabulary'
        assert 'significance' in data,\
            'serializer.data should contain an object called significance'
        assert 'code' in data,\
            'serializer.data should contain an object called code'

    def test_PolicyMarkerSerializer(self):
        policy_marker = iati_factory.PolicyMarkerFactory.build(code=1)
        serializer = serializers.ActivityPolicyMarkerSerializer.\
            PolicyMarkerSerializer(policy_marker)
        assert serializer.data['code'] == policy_marker.code,\
            "policy_marker.code should be serialized to a field called 'code'"

    def test_VocabularySerializer(self):
        vocabulary = iati_factory.VocabularyFactory.build(code=1)
        serializer = serializers.ActivityPolicyMarkerSerializer.\
            VocabularySerializer(vocabulary)
        assert serializer.data['code'] == str(vocabulary.code),\
            "vocabulary.code should be serialized to a field called 'code'"

    def test_PolicySignificanceSerializer(self):
        significance = iati_factory.PolicySignificanceFactory.build(code=1)
        serializer = serializers.ActivityPolicyMarkerSerializer.\
            PolicySignificanceSerializer(significance)
        assert serializer.data['code'] == significance.code,\
            "significance.code should be serialized to a field called 'code'"

    def test_TitleSerializer(self):
        activity = iati_factory.ActivityFactory.build(id=None)
        serializer = serializers.TitleSerializer(activity)
        assert 'narratives' in serializer.data,\
            "A serialized title should containt a object 'narratives'"

    def test_TitleNarrativesSerializer(self):
        title = iati_factory.TitleFactory.build(
            title='activity title',
            language=iati_factory.LanguageFactory.build(code='fr')
        )
        serializer = serializers.TitleSerializer.NarrativeSerializer(title)
        assert serializer.data['text'] == title.title,\
            "'title.title' should be serialized to a field called 'text'"
        assert serializer.data['language'] == title.language.code,\
            """
            'title.language' should be serialized to a field called 'language'
            """

    def test_DescriptionSerializer(self):
        description = iati_factory.DescriptionFactory.build(
            type=iati_factory.DescriptionTypeFactory.build(code=1)
        )
        serializer = serializers.DescriptionSerializer(description)
        assert serializer.data['type'] == description.type.code,\
            """
            'description.type.code' should be serialized to a field called
            'type'
            """

    def test_DescriptionNarrativeSerializer(seslf):
        description = iati_factory.DescriptionFactory.build(
            description='some text to describe an activity',
            language=iati_factory.LanguageFactory.build(code='fr'),
        )
        serializer = serializers.DescriptionSerializer.NarrativeSerializer(
            description)
        assert serializer.data['language'] == description.language.code,\
            """
            'description.language' should be serialized to a field called
            'language'
            """
        assert serializer.data['text'] == description.description,\
            """
            'description.description' should be serialid to a field called
            'text'
            """

    def test_ActivitySerializerDynamicFields(self):
        activity = iati_factory.ActivityFactory.build(
            id='identifier',
            iati_identifier='iati-identifier'
        )
        fields = ['id']
        serializer = serializers.ActivitySerializer(activity, fields=fields)
        assert serializer.data['id'] == 'identifier', \
            """
            activity.id should be serialized since it is specified with
            the fields parameter
            """
        assert 'iati_identifier' not in serializer.data, \
            """
            activity.iati_identifier should NOT be serialized since it is
            not specified in the fields parameter
            """

    def test_ActivitySectorSerializer(self):
        activity_sector = iati_factory.ActivitySectorFactory.build(
            percentage=80.00
        )
        serializer = serializers.ActivitySectorSerializer(
            activity_sector,
            context={'request': self.request_dummy},
        )
        assert serializer.data['percentage'] == '{0:.2f}'.format(
            activity_sector.percentage),\
            """
            'activity_sector.percentage' should be serialized to a field
            called percentage
            """
        assert 'sector' and 'vocabulary' in serializer.data,\
            """
            a serialized ActivitySector should contain the objects 'sector'
            and 'vocabulary'
            """
        assert 'url' and 'code' and 'name' in serializer.data['sector'],\
            """
            the serialized sector should contain the fields 'url, 'code', and
            'name'
            """

    def test_ActivitySectorVocabularySerializer(self):
        vocabulary = iati_factory.VocabularyFactory.build(
            code='DAC'
        )
        serializer = serializers.ActivitySectorSerializer.VocabularySerializer(
            vocabulary)
        assert serializer.data['code'] == vocabulary.code,\
            """
            'vocabulary.code' should be serialized to a field called 'code'
            """

    def test_ActivityRecipientRegionSerializer(self):
        recipient_region = iati_factory.ActivityRecipientRegionFactory.build(
            percentage=80)
        serializer = serializers.ActivityRecipientRegionSerializer(
            recipient_region,
            context={'request': self.request_dummy}
        )
        assert serializer.data['percentage'] == '{0:.2f}'.format(
            recipient_region.percentage),\
            """
            'recipient_region.percentage' should be serialized to a field
            called 'percentage'
            """
        assert 'region' and 'vocabulary' in serializer.data,\
            """
            a serialized RecipientRegion should contain the fields 'region'
            and 'vocabulary'
            """
        assert 'url' and 'code' and 'name' in serializer.data['region'],\
            """
            a region, serialized by the ActivityRecipientRegionSerializer
            should contain the fields 'url', 'code' and 'name'
            """

    def test_ActivityRecipientRegionVocabularySerializer(self):
        vocabulary = iati_factory.RegionVocabularyFactory.build(
            code=2,
        )
        serializer = serializers.ActivityRecipientRegionSerializer.\
            RegionVocabularySerializer(vocabulary)
        assert serializer.data['code'] == vocabulary.code,\
            """
            'vocabulary.code' should be serialized to a field called 'code'
            """

    def test_ParticipatingOrganisationSerializer(self):
        part_org = iati_factory.ParticipatingOrganisationFactory.build()
        serializer = serializers.ParticipatingOrganisationSerializer(
            part_org,
            context={'request': self.request_dummy}
        )
        assert 'organisation' and 'role' in serializer.data,\
            """
            a serialized ParticipatingOrganisation should contain the fields
            'organisation' and 'role'
            """
        assert 'url' and 'code' and 'name' in serializer.data['organisation'],\
            """
            the organisation serialized by ParticipatingOrganisationSerializer
            should contain the fields 'url', 'code' and 'name'
            """

    def test_ParticipatingOrganisationRoleSerializer(self):
        role = iati_factory.OrganisationRoleFactory.build(code=1)
        serializer = serializers.ParticipatingOrganisationSerializer.\
            OrganisationRoleSerializer(role)
        assert serializer.data['code'] == str(role.code),\
            """
            'role.code' should be serialized to a field called 'code'
            """

    def test_RecipientCountrySerializer(self):
        recipient_country = iati_factory.RecipientCountryFactory.build(
            percentage=80
        )
        serializer = serializers.RecipientCountrySerializer(
            recipient_country,
            context={'request': self.request_dummy}
        )
        assert serializer.data['percentage'] == '{0:.2f}'.format(
            recipient_country.percentage),\
            """
            'recipient_country.percentage' should be serialized to a field
            called 'percentage'
            """
        assert 'country' in serializer.data,\
            """
            a serialized RecipientCountry should contain the field 'country'
            """
        assert 'url' and 'code' and 'name' in serializer.data['country'],\
            """
            the serialized country should contain the fields 'url', 'code' and
            'name'
            """

    def test_ActivityScopeSerializer(self):
        activity_scope = iati_factory.ActivityScopeFactory.build(
            code=1,
            name='global',
        )
        serializer = serializers.ActivityScopeSerializer(activity_scope)
        assert serializer.data['code'] == activity_scope.code,\
            """
            'activity_scope.code' should be serialized to a field called
            'code'
            """

    def test_CurrencySerializer(self):
        currency = iati_factory.CurrencyFactory.build(code='EUR')
        serializer = serializers.CurrencySerializer(currency)
        assert serializer.data['code'] == currency.code,\
            """
            'currency.code' should be serialized to a field called
            'code'
            """

    def test_FinanceTypeSerializer(self):
        finance_type = iati_factory.FinanceTypeFactory.build(code=110)
        serializer = serializers.FinanceTypeSerializer(finance_type)
        assert serializer.data['code'] == finance_type.code,\
            """
            'finance_type.code' should be serialized to a field called
            'code'
            """

    def test_TiedStatusSerializer(self):
        tied_status = iati_factory.TiedStatusFactory.build(code=3)
        serializer = serializers.TiedStatusSerializer(tied_status)
        assert serializer.data['code'] == tied_status.code,\
            """
            'tied_status.code' should be serialized to a field called
            'code'
            """

    def test_CapitalSpendSerializer(self):
        activity = iati_factory.ActivityFactory.build(capital_spend=80)
        serializer = serializers.CapitalSpendSerializer(activity)
        assert serializer.data['percentage'] == '{0:.2f}'.format(activity.capital_spend),\
            """
            'activity.capital_spend' should be serialized to a field called
            'percentage'
            """

    @pytest.mark.django_db
    def test_activitySerializer(self):
        request_dummy = RequestFactory().get('/')
        activity = iati_factory.ActivityFactory.build(
            iati_identifier='IATI-0001',
            id='IATI-0001',
            last_updated_datetime='2014-12-03',
            hierarchy=1,
            linked_data_uri='www.data.example.org/123',
            xml_source_ref='www.data.example.org/123/1234.xml'
        )
        serializer = serializers.ActivitySerializer(
            activity, context={'request': request_dummy})
        assert serializer.data['id'] == activity.id,\
            """
            a serialized activity should contain a field 'id' that contains
            the data in activity.id
            """
        assert serializer.data['iati_identifier'] == activity.iati_identifier,\
            """
            a serialized activity should contain a field 'iati_identifier' that
            contains the data in activity.iati_identifier
            """

        assert serializer.data['last_updated_datetime'] ==\
            activity.last_updated_datetime,\
            """
            a serialized activity should contain a field 'last_updated_datetime
            that contains the data in activity.last_updated_datetime
            """
        assert serializer.data['hierarchy'] == activity.hierarchy,\
            """
            a serialized activity should contain a field 'hierarchy' that
            contains the data in activity.hierarchy
            """
        assert serializer.data['linked_data_uri'] == activity.linked_data_uri,\
            """
            a serialized activity should contain a field 'linked_data_uri'
            that contains the data in activity.linked_data_uri
            """
        assert serializer.data['xml_source_ref'] == activity.xml_source_ref,\
            """
            a serialized activity should contain a field 'xml_source_ref' that
            contains the data in activity.xml_source_ref
            """

    @pytest.mark.django_db
    def test_activitySerializer_required_fields(self):
        request_dummy = RequestFactory().get('/')
        activity = iati_factory.ActivityFactory.build()
        serializer = serializers.ActivitySerializer(
            activity, context={'request': request_dummy})

        required_fields = (
            'url',
            'id',
            'iati_identifier',
            'last_updated_datetime',
            'default_currency',
            'hierarchy',
            'linked_data_uri',
            'reporting_organisation',
            'title',
            'descriptions',
            'participating_organisations',
            'activity_status',
            'activity_dates',
            'activity_scope',
            'recipient_countries',
            'recipient_regions',
            'sectors',
            'policy_markers',
            'collaboration_type',
            'default_flow_type',
            'default_finance_type',
            'default_aid_type',
            'default_tied_status',
            'budgets',
            'capital_spend',

            'total_budget',
            'xml_source_ref',
        )
        assertion_msg = "the field '{0}' should be in the serialized activity"
        for field in required_fields:

            assert field in serializer.data, assertion_msg.format(field)