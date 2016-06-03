# Return parser functions for generic elements

from iati import models

def provider_org(self, parent_model, provider_model, fk_name):
    """
    parent_model: the model to which the provider_org will be applied
    provider_model: The provider_org model
    fk_name: the name of the foreign key back to the parent_model
    """

    def func(element):
        ref = element.attrib.get('ref', '')
        org_type = self.get_or_none(codelist_models.OrganisationType, code=element.attrib.get('type'))
        provider_activity_id = element.attrib.get('provider-activity-id')
        provider_activity = self.get_or_none(models.Activity, iati_identifier=provider_activity_id)

        normalized_ref = self._normalize(ref)
        organisation = self.get_or_none(models.Organisation, pk=ref)

        setattr(provider_model, fk_name, parent_model)
        provider_model.ref = ref
        provider_model.type = org_type
        provider_model.normalized_ref = normalized_ref
        provider_model.organisation = organisation
        provider_model.provider_activity_ref = provider_activity
        provider_model.provider_activity = provider_activity

        self.register_model(provider_model)

        # now add narrative(s)
        # for e in element.getchildren():
        #     self.add_narrative(element, provider_model)

        #     # workaround for IATI ref uniqueness limitation
        #     provider_model.primary_name = self.get_primary_name(element, provider_model.primary_name)

        return element

    return func


def receiver_org(self, parent_model, receiver_model, fk_name):
    """
    parent_model: the model to which the receiver_org will be applied
    receiver_model: The receiver_org model
    fk_name: the name of the foreign key back to the parent_model
    """

    def func(element):
        ref = element.attrib.get('ref', '')
        receiver_activity_id = element.attrib.get('receiver-activity-id')
        receiver_activity = self.get_or_none(models.Activity, iati_identifier=receiver_activity_id)

        normalized_ref = self._normalize(ref)
        organisation = self.get_or_none(models.Organisation, pk=ref)

        setattr(receiver_model, fk_name, parent_model)
        receiver_model.ref = ref
        receiver_model.normalized_ref = normalized_ref
        receiver_model.organisation = organisation
        receiver_model.receiver_activity_ref = receiver_activity
        receiver_model.receiver_activity = receiver_activity


        print(receiver_model)
        self.register_model(receiver_model)

        # # now add narrative(s)
        # for e in element.getchildren():
        #     self.add_narrative(element, receiver_model)

        #     # workaround for IATI ref uniqueness limitation
        #     receiver_model.primary_name = self.get_primary_name(element, receiver_model.primary_name)

        return element

    return func

