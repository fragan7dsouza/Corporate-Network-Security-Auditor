
from fpdf import FPDF
import datetime
import os
from utils.logger import log_info, log_error

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Corporate Network Security Audit Report', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 5, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, content_list):
        self.set_font('Arial', '', 10)
        
        if not content_list:
            self.cell(0, 5, "No issues detected. [OK]", 0, 1) 
        else:
            for item in content_list:
                self.set_text_color(255, 0, 0)
                self.cell(5, 5, "[X]", 0, 0) 
                self.set_text_color(0, 0, 0)
                self.multi_cell(0, 5, f"{item}", 0, 'L')
        self.ln(2)

def generate_pdf(ip, open_ports, vulnerabilities=None, firewall_issues=None, password_issues=None):
    """Generates the PDF report using the audit data."""
    pdf = PDFReport()
    pdf.add_page()
    
    pdf.chapter_title(f"Target Summary: {ip}")
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 5, f"Audit Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1)
    
    pdf.chapter_title("1. Open Ports Detected")
    pdf.set_font('Arial', '', 10)
    if open_ports:
        ports_str = ", ".join(map(str, open_ports))
        pdf.multi_cell(0, 5, ports_str)
    else:
        pdf.cell(0, 5, "No open ports found on scanned range. [SAFE]", 0, 1) 

    pdf.chapter_title("2. Service Vulnerabilities")
    pdf.chapter_body(vulnerabilities or [])

    pdf.chapter_title("3. Firewall Policy Analysis")
    pdf.chapter_body(firewall_issues or [])

    pdf.chapter_title("4. Password Policy Audit")
    pdf.chapter_body(password_issues or [])
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = f"scan_report_{ip}_{timestamp}.pdf"
    report_path = os.path.join("reports", report_name)

    try:
        pdf.output(report_path, 'F')
        log_info(f"PDF report successfully created: {report_path}")
        return report_path
    except Exception as e:
        log_error(f"Failed to generate PDF report: {e}")
        return None

if __name__ == "__main__":
    ports = [21, 80, 443]
    vulns = ["Port 21: Cleartext FTP detected.", "Port 80: HTTP exposed (no HTTPS)."]
    firewall = ["Port 21 is exposed."]
    passwords = ["Password too short."]
    
    pdf_path = generate_pdf("192.168.1.1", ports, vulns, firewall, passwords)
    if pdf_path:
        print(f"\n[✔] Test PDF generated: {pdf_path}")