from dbt.adapters.synapseserverless.connections import SynapseServerlessConnectionManager
from dbt.adapters.synapseserverless.connections import SynapseServerlessCredentials
from dbt.adapters.synapseserverless.impl import SynapseServerlessAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import synapseserverless


Plugin = AdapterPlugin(
    adapter=SynapseServerlessAdapter,
    credentials=SynapseServerlessCredentials,
    include_path=synapseserverless.PACKAGE_PATH,
    dependencies=['synapse']
)
