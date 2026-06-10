import re

def fix():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the PDF Generation Logic
    old_logic = """    ss.forEach(slide => {
      const clone = slide.cloneNode(true);
      clone.classList.add('on');
      printContainer.appendChild(clone);
    });"""

    new_logic = """    ss.forEach(slide => {
      const clone = slide.cloneNode(true);
      clone.classList.add('on');
      // Fix for PDF: Make clones position relative so they stack vertically
      clone.style.position = 'relative';
      // Ensure page break after each slide
      clone.style.pageBreakAfter = 'always';
      clone.style.overflow = 'hidden';
      printContainer.appendChild(clone);
    });
    
    // Position printContainer off-screen to not mess up viewport
    printContainer.style.position = 'absolute';
    printContainer.style.top = '0';
    printContainer.style.left = '-9999px';
"""

    if old_logic in content:
        content = content.replace(old_logic, new_logic)
        with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed")
    else:
        print("Not found")

fix()
