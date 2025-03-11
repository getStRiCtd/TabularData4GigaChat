import aiohttp
import pandas as pd

from src.config import md_api_conf

def array_to_df(headers: list, rows: list) -> pd.DataFrame:
    sample = pd.DataFrame(data=rows, columns=headers)
    return sample

def convert_df_to_html(df: pd.DataFrame) -> str:
    """
    Converts pd.DataFrame to HTML
    :param df:
    :return: HTML code in str format
    """
    return df.to_html()


async def convert_html_to_list_table(html: str):
    """
    Converts HTML table to list-table format.\n
    https://sublime-and-sphinx-guide.readthedocs.io/en/latest/tables.html

    If you haven't got access to MarkdownApi service, you should implement this converter by yourself.
    :param html: pure html table representation
    :return: table in list_table format
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=md_api_conf.convert_endpoint,
            json={"html": html},
            auth=md_api_conf.auth_token
        ) as response:
            response_json = await response.json()
            rst_table_str = response_json['markdown']
            return rst_table_str