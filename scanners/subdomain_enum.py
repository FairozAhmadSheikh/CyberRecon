import dns.resolver

def enumerate_subdomains(domain):
    wordlist = ['www', 'mail', 'ftp', 'admin', 'test', 'dev', 'api', 'portal']
    found = []
    resolver = dns.resolver.Resolver()
    resolver.timeout = 2
    resolver.lifetime = 2