import dns.resolver

def enumerate_subdomains(domain):
    wordlist = ['www', 'mail', 'ftp', 'admin', 'test', 'dev', 'api', 'portal']
    found = []