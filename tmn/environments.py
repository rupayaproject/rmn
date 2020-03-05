environments = {
    'mainnet': {
        'tomochain': {
            'BOOTNODES': (
                'enode://504e40653c81b62634aae3c75cb0804f933fa05006dc9f63e50dd'
                'a178a9b6fcd7de2360fcf77ccca93fe7e016d9e636b440c1db6d00053c251'
                '7130c240bed107@167.172.48.132:30301'
            ),
            'NETSTATS_HOST': 'wss://stats.rupaya.io',
            'NETSTATS_PORT': '443',
            'NETWORK_ID': '77',
            'WS_SECRET': (
                'universal-gas-lighter-fluid'
            )
        },
    },
    'testnet': {
        'tomochain': {
            'BOOTNODES': (
                'enode://ba966140e161ad416a7bd7c75dc695e0a41232723e2b19cbbf651'
                '883ef5e8f2528801b17b9d63152814d219a58a4fcc3e3c877486e64057523'
                'f6714092348efa@195.154.150.210:30301'
            ),
            'NETSTATS_HOST': 'stats.testnet.tomochain.com',
            'NETSTATS_PORT': '443',
            'NETWORK_ID': '89',
            'WS_SECRET': (
                '9tlu4EymcTrEzaqWpSxh3KSa926au8'
            )
        },
    },
    'devnet': {
        'tomochain': {
            'BOOTNODES': (
                'enode://5bec42d41c9eb291c1d20c9ac92bd9c86a4954189b6592b0833e5'
                'c28e389b59e3992efed119a2782d9b95ba7aa78e7f71813067cd6734fadff'
                '322f7dd6fc3b3c@104.248.99.234:30301,enode://89028bc15e9dda643'
                'bc4b9a1a6352896dd3bce7411543b0b160a9eb95093ddbe1f5eda5999e38a'
                '4874bfa6a00fb3526cc2fb9b4feb2a3f7cc80ef8016e05c493@104.248.99'
                '.235:30301,enode://ea8f1eb1a2a695960bfa6df52094c635e173c65e5f'
                'c120501672c0d21900d826d6c1c5a07d64ad36509ec5e7306d7a2c3398398'
                'f34f3e279b91c487c2b3a9537@104.248.99.233:30301'
            ),
            'NETSTATS_HOST': 'stats.devnet.tomochain.com',
            'NETSTATS_PORT': '443',
            'NETWORK_ID': '90',
            'WS_SECRET': (
                'torn-fcc-caper-drool-jelly-zip-din-fraud-rater-darn'
            )
        },
    }
}
