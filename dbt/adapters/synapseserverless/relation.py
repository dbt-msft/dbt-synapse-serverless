from typing import Optional

from dataclasses import dataclass

from dbt.adapters.base.relation import BaseRelation, Policy
from dbt.exceptions import RuntimeException

@dataclass
class SynapseServerlessIncludePolicy(Policy):
    database: bool = False
    schema: bool = True
    identifier: bool = True


@dataclass(frozen=True, eq=False, repr=False)
class SynapseServerlessRelation(BaseRelation):
    include_policy: SynapseServerlessIncludePolicy = SynapseServerlessIncludePolicy()