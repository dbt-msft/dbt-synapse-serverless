from dataclasses import dataclass
from dbt.adapters.sqlserver import (SQLServerConnectionManager,
                                    SQLServerCredentials)

@dataclass
class SynapseServerlessCredentials(SQLServerCredentials):

    @property
    def type(self):
        return "synapseserverless"

class SynapseServerlessConnectionManager(SQLServerConnectionManager):
    TYPE = "synapseserverless"
    TOKEN = None
