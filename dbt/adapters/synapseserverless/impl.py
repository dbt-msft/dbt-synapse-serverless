from dbt.adapters.synapse import SynapseAdapter
from dbt.adapters.synapseserverless import SynapseServerlessConnectionManager
from dbt.adapters.synapseserverless.relation import SynapseServerlessRelation



class SynapseServerlessAdapter(SynapseAdapter):
    Relation = SynapseServerlessRelation
    ConnectionManager = SynapseServerlessConnectionManager