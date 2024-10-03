# ScopeIt

This tiny repository aims to compute an IP addresses list based on inclusion and exclusion lists.

## Usage

The script takes files as parameters, containing IP addresses or CIDR, one per line.

```bash
$ cat included.txt
192.168.1.0/29
10.232.0.0/28
2.243.5.35

$ cat excluded.txt
192.168.1.4
10.232.0.0/29
4.4.32.5

$ ./scopeit.py included.txt -exclude excluded.txt > scope.txt

$ cat scope.txt
192.168.1.0
192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.5
192.168.1.6
192.168.1.7
10.232.0.8
10.232.0.9
10.232.0.10
10.232.0.11
10.232.0.12
10.232.0.13
10.232.0.14
10.232.0.15
2.243.5.35
```

## License

See [LICENSE](./LICENSE) file.
