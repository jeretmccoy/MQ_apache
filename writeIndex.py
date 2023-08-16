# Create a new 'index.html' file or overwrite if it already exists
with open('index.html', 'w') as file:
    
    # Start the HTML content
    file.write('<!DOCTYPE html>\n')
    file.write('<html lang="en">\n')
    file.write('<head>\n')
    file.write('    <meta charset="UTF-8">\n')
    file.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    file.write('    <title>Master Output and Charts</title>\n')
    file.write('</head>\n')
    file.write('<body>\n')

    # Embed the charts
    file.write('    <h2>Hits Over Time</h2>\n')
    file.write('    <img src="hits_over_time.png" alt="Hits Over Time Chart">\n')
    file.write('    <h2>Traffic Over Time</h2>\n')
    file.write('    <img src="traffic_over_time.png" alt="Traffic Over Time Chart">\n')
    
    # Display the master output text
    file.write('    <h2>Master Output</h2>\n')
    file.write('    <pre>\n')
    with open('master_output.txt', 'r') as master:
        for line in master:
            file.write(line)
    file.write('    </pre>\n')

    # End the HTML content
    file.write('</body>\n')
    file.write('</html>\n')
