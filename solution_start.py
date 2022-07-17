import argparse



def get_params() -> dict:
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--customers_location', required=False, default="./input_data/starter/customers.csv")
    parser.add_argument('--products_location', required=False, default="./input_data/starter/products.csv")
    parser.add_argument('--transactions_location', required=False, default="./input_data/starter/transactions/")
    parser.add_argument('--output_location', required=False, default="./output_data/outputs/")
    return vars(parser.parse_args())

args = parser.parse_args()
kwargs = {}
if args.output_location:
    kwargs = dict()
    for _kwarg in args.output_location:
        key, val = _kwarg.split('=')
        kwargs.update({key: eval(val)})

import rbm

if __name__ == "__main__":

    benchmarker = rbm.utils.Benchmark(customers_location=args.customers_location, products_location=args.products_location, **kwargs)
    benchmarks = benchmarker.execute(transactions_location=args.transactions_location, output_location=args.output_location)
    print('*************************** Benchmark Results ***************************')
    benchmarks.update(benchmarks['benchmark'])
    _ = benchmarks.pop('benchmark')
    benchmarks = [f'{key}: {val}' for key, val in benchmarks.items()]
    print('\n'.join(benchmarks))