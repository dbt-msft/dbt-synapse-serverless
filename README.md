# dbt-synapse-serverless

custom [dbt](https://www.getdbt.com) adapter for [Azure Synapse](https://azure.microsoft.com/en-us/services/synapse-analytics/) serverless pools. This adapter largely inherits from dbt-synapse, which itself inherits from dbt-sqlserver. For more info, see those repos.

## major differences b/w `dbt-synapse-serverless` and `dbt-synapse`
In serverless pools, you can't:
- make tables (except external)
- rename relations
- use three part names (only `schema.relation`)
## status & support
this adapter is an experiment, here be dragons! I really don't even recommend you use dbt with serverless
## Installation & Setup

This is not published to PyPI. for now, install from Github with:

```sh
pip install git+https://github.com/dbt-msft/dbt-synapse-serverless.git
```

### Caveats
1. You can't use the default or master database on a "built-in" serverless pool, because somehow they enmeshed with the spark pool. You must go to the master db and make a new db first. That is what you will use for the dbt project.
2. dbt won't stop  you from trying to make tables, but it's not going to work. I would welcome PRs if people wanna make that experience better
3. I don't expect this to be supported for much longer as changes to dbt-core will require tables to make things like tests work.


## Authentication

Please see the [Authentication section of dbt-sqlserver's README.md](https://github.com/dbt-msft/dbt-sqlserver#authentication).

The only difference is to provide the adapter type as `synapseserverless` so for example:

```yml
jaffle_shop:
  target: serverless
  outputs:
    serverless:
      type: synapseserverless
      driver: "ODBC Driver 17 for SQL Server"
      schema: dbo
      host: <serverlessendpoint>
      database: <serverlessdb>
      authentication: CLI
```

