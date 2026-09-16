import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Slide 12 changes
content = content.replace('<h1>Un plan estrat\u00e9gico de tres meses</h1>', '<h1>Construcci\u00f3n del plan estrat\u00e9gico</h1>')
content = content.replace('<div class="phase-num">FASE 1 \u2014 MES 1</div>', '<div class="phase-num">FASE 1 \u2014 INVESTIGACI\u00d3N</div>')
content = content.replace('<div class="phase-num">FASE 2 \u2014 SEMANA 3\u20144</div>', '<div class="phase-num">FASE 2 \u2014 AN\u00c1LISIS</div>')
content = content.replace('<div class="phase-num">FASE 3 \u2014 MES 2\u20143</div>', '<div class="phase-num">FASE 3 \u2014 DESARROLLO</div>')

# Fallback for encoding differences
content = content.replace('<h1>Un plan estratégico de tres meses</h1>', '<h1>Construcción del plan estratégico</h1>')
content = content.replace('<div class="phase-num">FASE 1 &mdash; MES 1</div>', '<div class="phase-num">FASE 1 &mdash; INVESTIGACIÓN</div>')
content = content.replace('FASE 1 \u2014 MES 1', 'FASE 1 &mdash; INVESTIGACIÓN')
content = content.replace('FASE 2 \u2014 SEMANA 3\u20144', 'FASE 2 &mdash; ANÁLISIS')
content = content.replace('FASE 3 \u2014 MES 2\u20143', 'FASE 3 &mdash; DESARROLLO')


# Slide 15 changes
content = content.replace('<h1>Lo que recibe Renovacore Pro al cierre de los tres meses</h1>', '<h1>Lo que recibe Renovacore Pro al cierre del proyecto</h1>')

pricing_html = '''
        <h3 style="margin-top:36px; font-size:22px;">Inversión y tiempos de entrega</h3>
        <div class="card-row" style="margin-top:16px;">
          <div class="card brass">
            <h3>Entrega estándar (30 a 40 días)</h3>
            <p style="font-size:24px; font-weight:700; color:var(--ink); margin-top:12px;">,550</p>
            <p>El ritmo de trabajo recomendado para la investigación de mercado, la definición estratégica y la creación de los materiales base.</p>
          </div>
          <div class="card good">
            <h3>Entrega acelerada (14 a 21 días)</h3>
            <p style="font-size:24px; font-weight:700; color:var(--ink); margin-top:12px;">,315</p>
            <p>Incluye un sobrecargo de  por prioridad en calendario. Ideal si el equipo de Renovacore Pro necesita arrancar campañas en el menor tiempo posible.</p>
          </div>
        </div>
        <p class="cta-line">'''

content = content.replace('<p class="cta-line">', pricing_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
