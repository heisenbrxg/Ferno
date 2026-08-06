import os

directory = r"e:\ADES FINAL\ades\buyer-file"

for filename in os.listdir(directory):
    if filename.endswith(".html") and filename != "service-bms.html":
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        modified = False

        # 1. Update Submenu in Nav (regular and dropdowns)
        # Check if BMS link is not already there
        if "service-bms.html" not in content:
            # Match Public Health Engineering in Navbar submenu
            if '<li><a href="service-phe.html">Public Health Engineering</a></li>' in content:
                content = content.replace(
                    '<li><a href="service-phe.html">Public Health Engineering</a></li>',
                    '<li><a href="service-phe.html">Public Health Engineering</a></li>\n                                                    <li><a href="service-bms.html">BMS &amp; IBMS</a></li>'
                )
                modified = True
            
            # Match Plumbing & PHE in Navbar submenu
            if '<li><a href="service-phe.html">Plumbing &amp; PHE</a></li>' in content:
                content = content.replace(
                    '<li><a href="service-phe.html">Plumbing &amp; PHE</a></li>',
                    '<li><a href="service-phe.html">Plumbing &amp; PHE</a></li>\n                        <li><a href="service-bms.html">BMS &amp; IBMS</a></li>'
                )
                modified = True

            # Match Public Health Engineering in Footer
            if '<li><a href="service-phe.html">Public Health Engineering</a></li>' in content:
                # We need to make sure we don't double replace. Since we already replaced above, we can do replacement if it matches without the indentation of the nav.
                # Actually, the string replacement will replace all occurrences. Since both Navbar and Footer might use the same exact tag, replacing all occurrences is perfectly correct!
                pass

        # 2. Update service-details / service-* sidebars
        if "service-sidebar" in content and "service-bms.html" not in content:
            # Let's find the service list and append BMS before </ul>
            # Sidebars usually contain the list of service page links: service-phe.html and then </ul>
            if 'service-phe.html" class="text-dark text-decoration-none hover-primary d-block p-2 rounded">Public Health Engineering</a></li>\n                                    </ul>' in content:
                content = content.replace(
                    'service-phe.html" class="text-dark text-decoration-none hover-primary d-block p-2 rounded">Public Health Engineering</a></li>\n                                    </ul>',
                    'service-phe.html" class="text-dark text-decoration-none hover-primary d-block p-2 rounded">Public Health Engineering</a></li>\n                                        <li class="mb-2"><a href="service-bms.html" class="text-dark text-decoration-none hover-primary d-block p-2 rounded">BMS &amp; IBMS</a></li>\n                                    </ul>'
                )
                modified = True
            elif 'service-phe.html" class="text-dark text-decoration-none hover-primary d-block p-2 rounded bg-primary">Public Health Engineering</a></li>\n                                    </ul>' in content:
                content = content.replace(
                    'service-phe.html" class="text-dark text-decoration-none hover-primary d-block p-2 rounded bg-primary">Public Health Engineering</a></li>\n                                    </ul>',
                    'service-phe.html" class="text-dark text-decoration-none hover-primary d-block p-2 rounded bg-primary">Public Health Engineering</a></li>\n                                        <li class="mb-2"><a href="service-bms.html" class="text-dark text-decoration-none hover-primary d-block p-2 rounded">BMS &amp; IBMS</a></li>\n                                    </ul>'
                )
                modified = True

        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filename}")
        else:
            print(f"No changes for {filename}")
