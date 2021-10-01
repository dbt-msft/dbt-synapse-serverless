{# TODO Actually Implement the rename index piece #}
{# TODO instead of deleting it...  #}
{% macro synapseserverless__rename_relation(from_relation, to_relation) -%}
    {{ exceptions.raise_compiler_error(
        "renaming relations is not supported in serverless pools"
        )
    }}
{% endmacro %}

{% macro synapseserverless__create_table_as(temporary, relation, sql) -%}
    {{ exceptions.raise_compiler_error(
        "creating tables is not supported in serverless pools"
        )
    }}
{% endmacro %}

{% macro synapseserverless__get_columns_in_relation(relation) -%}
    {{ exceptions.raise_compiler_error("""
      getting columns in relation is not supported in serverless pools because
      1) there is no info schema for temp tables,
      2) nor are there tables at all!
    """
        )
    }}
{% endmacro %}
