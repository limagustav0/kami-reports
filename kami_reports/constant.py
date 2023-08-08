# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

import numpy as np
APP_VERSION = "0.3.2"
TIMEOUT = 3600
PAGE_SIZE = 100
OPERATORS = [
    ['ge ', '>='],
    ['le ', '<='],
    ['lt ', '<'],
    ['gt ', '>'],
    ['ne ', '!='],
    ['eq ', '='],
    ['contains '],
    ['datestartswith '],
]

MONTHS_PTBR = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro',
}
MONTHS_PTBR_ABBR = {
    1: 'JAN',
    2: 'FEV',
    3: 'MAR',
    4: 'ABR',
    5: 'MAI',
    6: 'JUN',
    7: 'JUL',
    8: 'AGO',
    9: 'SET',
    10: 'OUT',
    11: 'NOV',
    12: 'DEZ',
}

TAGS = ['_liquido', '_bruto', '_desconto', '_bonificado', '_enxoval']
STARTING_YEAR = 2022
CURRENT_MONTH = datetime.now().month
CURRENT_YEAR = datetime.now().year
COLUMNS_NAMES_HEAD = [
    'cod_colaborador',
    'nome_colaborador',
    'cod_cliente',
    'nome_cliente',
    'razao_social',
    'ramo_atividade',
    'dt_cadastro',
    'bairro',
    'cidade',
    'uf',
    'endereco',
    'numero',
    'cep',
    'dias_atraso',
    'valor_devido',
    'dt_primeira_compra',
    'dt_ultima_compra',
    'cod_marca',
    'desc_marca',
    'STATUS',
    'equipe',
]
SALE_NOPS = [
    '6.102',
    '6.404',
    'BLACKFRIDAY',
    'VENDA',
    'VENDA_S_ESTOQUE',
    'WORKSHOP',
]
SUBSIDIZED_NOPS = [
    'BONIFICADO',
    'BONIFICADO_F',
    'BONI_COMPRA',
    'PROMOCAO',
    'PROMO_BLACK',
    'CAMPANHA',
]
TROUSSEAU_NOPS = ['ENXOVAL']
COMPANIES = {
    1: 'KAMI CO',
    2: 'NEW HAUSS',
    3: 'MOVEMENT SP',
    4: 'ENERGY',
    5: 'HAIRPRO',
    6: 'SOUTH',
    9: 'MMS',
    10: '3MKO MATRIZ',
    11: '3MKO FILIAL SP',
    12: '3MKO FILIAL ES',
    13: 'MOVEMENT RJ',
    14: '3MKO FILIAL PR',
    15: 'MOVEMENT MT',
    16: 'MOVEMENT RS',
}
TEMPLATE_COLS = [
    'ano',
    'mes',
    'cod_cliente',
    'nome_cliente',
    'ramo_atividade',
    'bairro',
    'cidade',
    'uf',
    'cod_colaborador',
    'nome_colaborador',
    'cod_situacao',
    'desc_situacao',
    'cod_grupo_produto',
    'desc_grupo_produto',
    'cod_grupo_pai',
    'desc_grupo_pai',
    'cod_marca',
    'desc_marca',
    'empresa_nota_fiscal',
]

CUSTOMER_DETAILS_NUM_COLS = {
    'cod_cliente': np.int64,
    'dias_atraso': np.int64,
    'valor_devido': np.float64,
    'ultimo_ano_ativo': np.int64,
}
CUSTOMER_DETAILS_DATETIME_COLS = [
    'data_cadastro',
    'dt_primeira_compra',
    'dt_ultima_compra',
]
DAILY_BILLINGS_NUM_COLS = {
    'ano': np.int64,
    'mes': np.int64,
    'empresa_pedido': np.int64,
    'empresa_nota_fiscal': np.int64,
    'cod_cliente': np.int64,
    'cod_colaborador': np.int64,
    'cod_pedido': np.int64,
    'cod_situacao': np.int64,
    'cod_grupo_produto': np.int64,
    'cod_grupo_pai': np.int64,
    'cod_marca': np.int64,
    'custo_total': np.float64,
    'custo_kami': np.float64,
    'qtd': np.int64,
    'preco_unit_original': np.float64,
    'preco_total_original': np.float64,
    'margem_bruta': np.float64,
    'preco_total': np.float64,
    'preco_desconto_rateado': np.float64,
    'vl_total_pedido': np.float64,
    'desconto_pedido': np.float64,
    'valor_nota': np.float64,
    'total_bruto': np.float64,
}
MONTHLY_BILLINGS_NUM_COLS = {
    'ano': np.int64,
    'mes': np.int64,
    'cod_empresa': np.int64,
    'cod_pedido': np.int64,
    'cod_cliente': np.int64,
    'situacao_pedido': np.int64,
    'cod_colaborador': np.int64,
    'qtd': np.int64,
    'custo_total': np.float64,
    'custo_kami': np.float64,
    'preco_unit_original': np.float64,
    'preco_total_original': np.float64,
    'margem_bruta': np.float64,
    'preco_total': np.float64,
    'preco_desconto_rateado': np.float64,
    'vl_total_pedido': np.float64,
    'desconto_pedido': np.float64,
    'valor_nota': np.float64,
    'situacao_entrega': np.int64,
    'empresa_pedido': np.int64,
    'empresa_nf': np.int64,
}
MONTHLY_BILLINGS_SCRIPT = 'SELECT * FROM vw_monthly_billings'
DAILY_BILLINGS_SCRIPT = f'SELECT * FROM vw_daily_billings AS vdb \
    WHERE vdb.ano >= {STARTING_YEAR}'
CUSTOMER_DETAILS_SCRIPT = f'SELECT * FROM vw_customer_details AS vcd WHERE vcd.ultimo_ano_ativo >= {STARTING_YEAR}'
BILLINGS_DATETIME_COLS = [
    'dt_implante_pedido',
    'dt_entrega_comprometida',
    'dt_faturamento',
]
SALES_TEAMS = {
    1: 'Tiago Maruyama',   
    112: 'Tiago Maruyama',
    117: 'Tiago Maruyama',
    120: 'Carlos Benia',
    128: 'Tiago Maruyama',
    13: 'Adriana David',
    132: 'Tiago Maruyama',
    14: 'Adriana David',
    140: 'Marketing',
    146: 'Uso Próprio',
    148: 'Rogerio Casado',
    15: 'Sávio Almeida',
    153: 'Adriana David',
    154: 'Herbert Marcondes',
    158: 'Rogerio Casado',
    16: 'Uso Próprio',
    161: 'Adriana David',
    17: 'Adriana David',
    18: 'Carlos Gouveia',
    211: 'Maisa Ekermann',
    215: 'Alexandre Nascimento',
    217: 'Rogerio Casado',
    22: 'Adriana David',
    222: 'Adriana David',
    23: 'Herbert Marcondes',
    231: 'Uso Próprio',
    24: 'Sávio Almeida',
    253: 'Renato Mimoto',
    254: 'Carlos Gouveia',
    27: 'Adriana David',
    303: 'Amanda Bêtta',
    306: 'Amanda Bêtta',
    31: 'Sávio Almeida',
    315: 'Amanda Bêtta',
    317: 'Maisa Ekermann',
    327: 'Renato Mimoto',
    329: 'Rogerio Casado',
    330: 'Rogerio Casado',
    3334: 'Herbert Marcondes',
    3337: 'Alexandre Nascimento',
    3339: 'Maisa Ekermann',
    3342: 'Alexandre Nascimento',
    3343: 'Lauegis Miranda',
    3346: 'Uso Próprio',
    3348: 'Alexandre Nascimento',
    3349: 'Adriana David',
    3351: 'Maurício Rodrigues',
    3352: 'Alexandre Nascimento',
    3354: 'Alexandre Nascimento',
    3356: 'Saiu',
    3358: 'Alexandre Nascimento',
    3360: 'Tiago Maruyama',
    3361: 'Sávio Almeida',
    3362: 'Carlos Gouveia',
    3364: 'Alexandre Nascimento',
    3366: 'Alexandre Nascimento',
    3369: 'Alexandre Nascimento',
    3370: 'Alexandre Nascimento',
    3374: 'Alexandre Nascimento',
    3375: 'Alexandre Nascimento',
    3376: 'Alexandre Nascimento',
    3383: 'Merchandising',
    3387: 'Uso Próprio',
    3389: 'Amanda Bêtta',
    3391: 'Maisa Ekermann',
    3395: 'Uso Próprio',
    3400: 'Herbert Marcondes',
    3405: 'Alexandre Nascimento',
    3406: 'Alexandre Nascimento',
    3407: 'Alexandre Nascimento',
    3408: 'Alexandre Nascimento',
    3410: 'Sávio Almeida',
    3412: 'Maisa Ekermann',
    3414: 'Carlos Benia',
    3416: 'Herbert Marcondes',
    3420: 'Alexandre Nascimento',
    3423: 'Sávio Almeida',
    3424: 'Sávio Almeida',
    3425: 'Sávio Almeida',
    3436: 'Uso Próprio',
    3450: 'Carlos Benia',
    3451: 'Carlos Benia',
    349: 'Lauegis Miranda',
    35: 'Alexandre Nascimento',
    350: 'Lauegis Miranda',
    352: 'Herbert Marcondes',
    358: 'Maisa Ekermann',
    359: 'Rogerio Casado',
    36: 'Uso Próprio',
    360: 'Tiago Maruyama',
    364: 'Maisa Ekermann',
    370: 'Tiago Maruyama',
    371: 'Maisa Ekermann',
    376: 'Alexandre Nascimento',
    378: 'Alexandre Nascimento',
    38: 'Renato Mimoto',
    381: 'Adriana David',
    383: 'Maisa Ekermann',
    385: 'Alexandre Nascimento',
    387: 'Maurício Rodrigues',
    394: 'Promotora',
    4: 'Renato Mimoto',
    41: 'Adriana David',
    43: 'Adriana David',
    45: 'Adriana David',
    49: 'Herbert Marcondes',
    52: 'Renato Mimoto',
    53: 'Adriana David',
    54: 'Sávio Almeida',
    56: 'Renato Mimoto',
    57: 'Alexandre Nascimento',
    58: 'Adriana David',
    6: 'Adriana David',
    61: 'Herbert Marcondes',
    66: 'Sávio Almeida',
    72: 'Tiago Maruyama',
    77: 'Adriana David',
    78: 'Adriana David',
    79: 'Tiago Maruyama',
    85: 'Rogerio Casado',
    89: 'Sávio Almeida',
    9994: 'Saiu',
    9995: 'Marketing',
    9996: 'Promotora',
    9997: 'Merchandising',
    9998: 'Herbert Marcondes',
    9999: 'Uso Próprio',
}
