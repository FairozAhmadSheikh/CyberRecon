import dns.resolver

def enumerate_subdomains(domain):
    wordlist = ['www', 'mail', 'ftp', 'admin', 'test', 'dev', 'api', 'portal']
    found = []
    resolver = dns.resolver.Resolver()
    resolver.timeout = 2
    resolver.lifetime = 2
    for sub in wordlist:
        subdomain = f"{sub}.{domain}"
        try:
            answers = resolver.resolve(subdomain, 'A')
            ips = [rdata.to_text() for rdata in answers]
            found.append({'subdomain': subdomain, 'ip': ips})
        except:
            continue
    return found