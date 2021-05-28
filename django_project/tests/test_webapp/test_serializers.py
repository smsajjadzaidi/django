# import pytest
# import factory
#
# from rest_framework.fields import CharField
#
# from apps.transaction.api.serializers import CurrencySerializer, UnfilledTransactionSerializer, FilledTransactionSerializer
# from tests.test_transaction.factories import CurrencyFactory, UnfilledTransactionFactory, FilledTransactionFactory
#
#
# class TestCurrencySerializer:
#
#     @pytest.mark.unit
#     def test_serialize_model(self):
#         currency = CurrencyFactory.build()
#         serializer = CurrencySerializer(currency)
#
#         assert serializer.data
#
#     @pytest.mark.unit
#     def test_serialized_data(self, mocker):
#         valid_serialized_data = factory.build(
#             dict,
#             FACTORY_CLASS=CurrencyFactory
#         )
#
#         serializer = CurrencySerializer(data=valid_serialized_data)
#
#         assert serializer.is_valid()
#         assert serializer.errors == {}