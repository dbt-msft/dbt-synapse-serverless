from dbt.adapters.synapse import SynapseAdapter
from dbt.adapters.synapseserverless import SynapseServerlessConnectionManager



class SynapseServerlessAdapter(SynapseAdapter):
    ConnectionManager = SynapseServerlessConnectionManager