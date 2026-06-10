import sys

def patch_file():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Patch CSS variables
    content = content.replace('--G:#A91831; --N:#202221; --W:#fff;\n  --G2:#7a1020; --N2:#161a19;\n  --g40:#999; --g75:#404040;', '--G:#a81832; --N:#202221; --W:#fff;\n  --G2:#7a1020; --N2:#161a19;\n  --g40:#999; --g75:#404040;')

    # 2. Patch CSS to add #pdf-btn styles
    css_patch = """#sn{font-family:var(--fB);font-size:10px;color:rgba(255,255,255,.35);min-width:28px;text-align:center}
#pdf-btn{font-family:var(--fB);font-size:11px;font-weight:700;color:var(--W);background:var(--G);padding:6px 12px;border-radius:20px;border:none;cursor:pointer;margin-left:8px;transition:opacity .2s}
#pdf-btn:hover{opacity:.8}
/* Container for PDF Generation */
#print-container { position: absolute; left: -9999px; top: 0; width: 1920px; }
#print-container .s { position: relative; opacity: 1; pointer-events: auto; page-break-after: always; }
</style>
</head>"""
    content = content.replace('#sn{font-family:var(--fB);font-size:10px;color:rgba(255,255,255,.35);min-width:28px;text-align:center}\n</style>\n</head>', css_patch)

    # 3. Patch HTML to add button and script tag
    html_patch = """</div></div>
<div id="nav">
  <button id="prev">&#8592;</button>
  <div class="dots" id="dots"></div>
  <button id="next">&#8594;</button>
  <span id="sn">1/9</span>
  <button id="pdf-btn">PDF</button>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
<script>"""
    content = content.replace('</div></div>\n<div id="nav">\n  <button id="prev">&#8592;</button>\n  <div class="dots" id="dots"></div>\n  <button id="next">&#8594;</button>\n  <span id="sn">1/9</span>\n</div>\n<script>', html_patch)

    # 4. Patch JS to add PDF download logic
    js_patch = """  document.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key===' ')go(c+1);if(e.key==='ArrowLeft')go(c-1)});
  function rs(){const s=Math.min(window.innerWidth/1920,window.innerHeight/1080);sc.style.transform='scale('+s+')'}
  window.addEventListener('resize',rs);rs();

  // PDF Generation Logic
  document.getElementById('pdf-btn').addEventListener('click', function() {
    const originalBtnText = this.textContent;
    this.textContent = 'Generando...';
    this.disabled = true;

    const printContainer = document.createElement('div');
    printContainer.id = 'print-container';
    document.body.appendChild(printContainer);

    ss.forEach(slide => {
      const clone = slide.cloneNode(true);
      clone.classList.add('on');
      printContainer.appendChild(clone);
    });

    html2pdf().set({
      margin: 0,
      filename: 'Presentacion_ENAE.pdf',
      image: { type: 'jpeg', quality: 0.98 },
      html2canvas: { scale: 2, useCORS: true, letterRendering: true },
      jsPDF: { unit: 'px', format: [1920, 1080], orientation: 'landscape' }
    }).from(printContainer).save().then(() => {
      document.body.removeChild(printContainer);
      this.textContent = originalBtnText;
      this.disabled = false;
    });
  });
})();
</script>
</body>"""
    content = content.replace("  document.addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key===' ')go(c+1);if(e.key==='ArrowLeft')go(c-1)});\n  function rs(){const s=Math.min(window.innerWidth/1920,window.innerHeight/1080);sc.style.transform='scale('+s+')'}\n  window.addEventListener('resize',rs);rs();\n})();\n</script>\n</body>", js_patch)

    with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
        f.write(content)

patch_file()
