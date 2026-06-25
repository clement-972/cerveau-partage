#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cockpit du Cerveau Partage
==========================
Genere une page HTML autonome (cockpit.html) a partir des fichiers Markdown
du dossier cerveau/. Lecture seule : ne modifie aucune fiche, n'ecrit jamais
dans le cerveau (respecte la regle "pas d'ecriture sans MAJ cerveau").

Usage :
    python3 generate.py [chemin_du_dossier_cerveau]

Par defaut, le dossier cerveau est le parent du dossier contenant ce script
(le script vit dans cerveau/_cockpit/generate.py).
"""

import os
import re
import sys
import json
import datetime

# ---------------------------------------------------------------------------
# Metadonnees des dossiers (table d'aiguillage)
# ---------------------------------------------------------------------------
FOLDERS = [
    {"id": "01_reglementaire",       "label": "Reglementaire",        "icon": "&#9878;",  "subject": "Conformite, obligations legales",   "examples": "RGPD, normes, mentions obligatoires, facturation electronique", "accent": "#d97706"},
    {"id": "02_specs_fonctionnelles","label": "Specs fonctionnelles", "icon": "&#129513;","subject": "Comportement du produit",            "examples": "parcours utilisateur, regles metier, fonctionnalites, cas limites", "accent": "#2563eb"},
    {"id": "03_specs_techniques",    "label": "Specs techniques",     "icon": "&#128295;","subject": "Realisation technique",             "examples": "architecture, API, schema de donnees, stack, implementation", "accent": "#0d9488"},
    {"id": "04_skills",              "label": "Skills",               "icon": "&#129302;","subject": "Travail avec l'IA",                 "examples": "prompts, skills, procedures reutilisables, methodes de travail", "accent": "#7c3aed"},
    {"id": "05_roadmap",             "label": "Roadmap",              "icon": "&#129517;","subject": "Direction produit",                "examples": "vision, priorites, jalons, ce qui est prevu plus tard", "accent": "#db2777"},
    {"id": "06_en_cours",            "label": "En cours",             "icon": "&#128293;","subject": "Sujets non stabilises",            "examples": "decisions en cours, questions ouvertes, travaux a trancher", "accent": "#dc2626"},
]

IGNORE_NAMES = {"Icon", "Icon\r", ".DS_Store", "cockpit.html"}
IGNORE_DIRS = {".tmp.driveupload", "_cockpit"}


def parse_header(body):
    """Extrait les metadonnees de la ligne d'en-tete (> Statut : ... | ...)."""
    meta = {"statut": "", "maj": "", "auteur": "", "motscles": []}
    m = re.search(r"^\s*>\s*(.+)$", body, re.MULTILINE)
    if not m:
        return meta, body
    line = m.group(1)
    for part in line.split("|"):
        part = part.strip()
        low = part.lower()
        if low.startswith("statut") or low.startswith("status"):
            meta["statut"] = part.split(":", 1)[-1].strip()
        elif "maj" in low or "update" in low or "derniere" in low:
            meta["maj"] = part.split(":", 1)[-1].strip()
        elif low.startswith("auteur") or low.startswith("author"):
            meta["auteur"] = part.split(":", 1)[-1].strip()
        elif "mots" in low or "keyword" in low:
            kw = part.split(":", 1)[-1].strip()
            meta["motscles"] = [k.strip() for k in re.split(r"[,;]", kw) if k.strip()]
    # retire la ligne d'en-tete du corps
    cleaned = body[:m.start()] + body[m.end():]
    return meta, cleaned


def parse_note(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        raw = f.read()
    # titre = premier H1
    title_m = re.search(r"^#\s+(.+)$", raw, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else os.path.basename(path)
    # corps sans le H1
    if title_m:
        body = raw[:title_m.start()] + raw[title_m.end():]
    else:
        body = raw
    meta, body = parse_header(body)
    body = body.strip("\n")
    filename = os.path.basename(path)
    is_example = filename.startswith("_exemple")
    return {
        "title": title,
        "file": filename,
        "statut": meta["statut"],
        "maj": meta["maj"],
        "auteur": meta["auteur"],
        "motscles": meta["motscles"],
        "body": body,
        "is_example": is_example,
        "wordcount": len(re.findall(r"\w+", body)),
    }


def build_data(root):
    folders_out = []
    total_notes = 0
    total_examples = 0
    all_dates = []
    for fdef in FOLDERS:
        fpath = os.path.join(root, fdef["id"])
        notes = []
        if os.path.isdir(fpath):
            for name in sorted(os.listdir(fpath)):
                if name in IGNORE_NAMES or not name.endswith(".md"):
                    continue
                note = parse_note(os.path.join(fpath, name))
                notes.append(note)
                if note["is_example"]:
                    total_examples += 1
                else:
                    total_notes += 1
                    if note["maj"]:
                        all_dates.append(note["maj"])
        entry = dict(fdef)
        entry["notes"] = notes
        entry["count_real"] = sum(1 for n in notes if not n["is_example"])
        entry["count_example"] = sum(1 for n in notes if n["is_example"])
        folders_out.append(entry)

    # Contexte (conventions)
    contexte = ""
    cpath = os.path.join(root, "00_CONTEXTE.md")
    if os.path.isfile(cpath):
        with open(cpath, "r", encoding="utf-8", errors="replace") as f:
            contexte = f.read()

    # Journal
    journal_rows = []
    jpath = os.path.join(root, "00_JOURNAL.md")
    if os.path.isfile(jpath):
        with open(jpath, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line.startswith("|"):
                    continue
                cells = [c.strip() for c in line.strip("|").split("|")]
                if len(cells) < 4:
                    continue
                if cells[0].lower() in ("date", "") or set(cells[0]) <= {"-", ":", " "}:
                    continue
                journal_rows.append({
                    "date": cells[0], "auteur": cells[1],
                    "fichier": cells[2], "resume": cells[3],
                })

    last_update = max(all_dates) if all_dates else (
        journal_rows[0]["date"] if journal_rows else "")

    return {
        "folders": folders_out,
        "contexte": contexte,
        "journal": journal_rows,
        "stats": {
            "notes": total_notes,
            "examples": total_examples,
            "folders": sum(1 for f in folders_out if f["notes"]),
            "folders_total": len(FOLDERS),
            "journal": len(journal_rows),
            "last_update": last_update,
        },
    }


# ---------------------------------------------------------------------------
# Gabarit HTML (autonome : CSS + JS + rendu Markdown integres)
# ---------------------------------------------------------------------------
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cockpit du Cerveau partage</title>
<style>
  :root{
    --bg:#f4f5fb; --surface:#ffffff; --surface-2:#fafbff; --ink:#181a2a;
    --muted:#646b8a; --line:#e7e9f4; --accent:#5b4ddb; --accent-soft:#ece9ff;
    --shadow:0 1px 2px rgba(24,26,42,.05),0 8px 24px -12px rgba(24,26,42,.18);
    --radius:16px;
  }
  *{box-sizing:border-box}
  html,body{margin:0;padding:0}
  body{
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    background:
      radial-gradient(1200px 600px at 100% -10%, #efeaff 0%, transparent 55%),
      radial-gradient(1000px 500px at -10% 0%, #e6f0ff 0%, transparent 50%),
      var(--bg);
    color:var(--ink); -webkit-font-smoothing:antialiased; line-height:1.55;
    min-height:100vh;
  }
  a{color:var(--accent);text-decoration:none}
  a:hover{text-decoration:underline}
  .wrap{max-width:1180px;margin:0 auto;padding:0 22px}

  /* ---- Top bar ---- */
  header.top{position:sticky;top:0;z-index:30;backdrop-filter:saturate(1.4) blur(10px);
    background:rgba(244,245,251,.82);border-bottom:1px solid var(--line)}
  .top-inner{display:flex;align-items:center;gap:18px;padding:14px 22px;max-width:1180px;margin:0 auto}
  .brand{display:flex;align-items:center;gap:12px;cursor:pointer;user-select:none}
  .brand .logo{width:40px;height:40px;border-radius:12px;flex:none;
    background:linear-gradient(135deg,#6c5ce7,#8e7bff);display:grid;place-items:center;
    color:#fff;font-size:20px;box-shadow:0 6px 18px -6px rgba(108,92,231,.7)}
  .brand h1{font-size:16px;margin:0;letter-spacing:-.01em}
  .brand p{margin:0;font-size:12px;color:var(--muted)}
  .search{margin-left:auto;position:relative;flex:1;max-width:420px}
  .search input{width:100%;padding:11px 14px 11px 40px;border:1px solid var(--line);
    border-radius:12px;background:var(--surface);font-size:14px;color:var(--ink);
    outline:none;transition:border-color .15s,box-shadow .15s}
  .search input:focus{border-color:var(--accent);box-shadow:0 0 0 4px var(--accent-soft)}
  .search .si{position:absolute;left:13px;top:50%;transform:translateY(-50%);opacity:.5;font-size:15px}
  .search kbd{position:absolute;right:10px;top:50%;transform:translateY(-50%);font-size:11px;
    color:var(--muted);background:var(--surface-2);border:1px solid var(--line);
    border-radius:6px;padding:2px 6px}

  /* ---- Layout ---- */
  .layout{display:grid;grid-template-columns:236px 1fr;gap:28px;padding:28px 0 80px}
  nav.side{position:sticky;top:84px;align-self:start;display:flex;flex-direction:column;gap:4px}
  nav.side .navlabel{font-size:11px;text-transform:uppercase;letter-spacing:.08em;
    color:var(--muted);margin:6px 10px 4px;font-weight:600}
  .navitem{display:flex;align-items:center;gap:10px;padding:9px 11px;border-radius:10px;
    cursor:pointer;font-size:14px;color:var(--ink);transition:background .12s;border:1px solid transparent}
  .navitem:hover{background:var(--surface)}
  .navitem.active{background:var(--surface);border-color:var(--line);box-shadow:var(--shadow);font-weight:600}
  .navitem .ic{width:26px;height:26px;border-radius:8px;display:grid;place-items:center;
    font-size:14px;background:var(--accent-soft);flex:none}
  .navitem .badge{margin-left:auto;font-size:11px;color:var(--muted);background:var(--surface-2);
    border:1px solid var(--line);border-radius:20px;padding:1px 8px;min-width:22px;text-align:center}
  main{min-width:0}

  /* ---- Hero ---- */
  .hero{background:linear-gradient(135deg,#fff, #fbfaff);border:1px solid var(--line);
    border-radius:var(--radius);padding:26px 28px;box-shadow:var(--shadow);margin-bottom:24px;
    position:relative;overflow:hidden}
  .hero:after{content:"";position:absolute;right:-60px;top:-60px;width:220px;height:220px;
    background:radial-gradient(circle,#efeaff,transparent 70%);pointer-events:none}
  .hero h2{margin:0 0 6px;font-size:24px;letter-spacing:-.02em}
  .hero p{margin:0;color:var(--muted);font-size:14px;max-width:640px}
  .stats{display:flex;gap:26px;margin-top:20px;flex-wrap:wrap}
  .stat{display:flex;flex-direction:column}
  .stat b{font-size:24px;letter-spacing:-.02em}
  .stat span{font-size:12px;color:var(--muted)}

  .sectiontitle{font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);
    font-weight:700;margin:30px 2px 14px}

  /* ---- Folder cards ---- */
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:16px}
  .card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);
    padding:18px;box-shadow:var(--shadow);cursor:pointer;transition:transform .14s,box-shadow .14s;
    position:relative;overflow:hidden}
  .card:hover{transform:translateY(-3px);box-shadow:0 14px 32px -16px rgba(24,26,42,.35)}
  .card .topbar{height:4px;border-radius:4px;width:42px;margin-bottom:14px}
  .card .ic{font-size:24px;margin-bottom:8px}
  .card h3{margin:0 0 4px;font-size:16px;letter-spacing:-.01em}
  .card .sub{font-size:13px;color:var(--muted);margin:0 0 10px}
  .card .ex{font-size:12px;color:var(--muted);opacity:.85;margin:0}
  .card .count{position:absolute;top:16px;right:16px;font-size:12px;font-weight:600;
    background:var(--surface-2);border:1px solid var(--line);border-radius:20px;padding:3px 10px}

  /* ---- Note cards ---- */
  .notecard{background:var(--surface);border:1px solid var(--line);border-radius:14px;
    padding:16px 18px;box-shadow:var(--shadow);cursor:pointer;transition:transform .12s,box-shadow .12s;margin-bottom:12px}
  .notecard:hover{transform:translateY(-2px);box-shadow:0 12px 28px -16px rgba(24,26,42,.32)}
  .notecard h3{margin:0 0 6px;font-size:16px;letter-spacing:-.01em}
  .notemeta{display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:12px;color:var(--muted)}
  .chip{font-size:11px;border-radius:20px;padding:2px 9px;border:1px solid var(--line);background:var(--surface-2)}
  .chip.kw{background:var(--accent-soft);border-color:transparent;color:#4a3fc0}
  .badge-status{font-size:11px;font-weight:600;border-radius:20px;padding:2px 10px}
  .st-stable{background:#e6f7ed;color:#0a7d3c}
  .st-encours{background:#fff1e6;color:#c2620a}
  .st-example{background:#eef0f6;color:#727a96}
  .excerpt{color:var(--muted);font-size:13px;margin:8px 0 0;display:-webkit-box;
    -webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}

  /* ---- Note reader ---- */
  .reader{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);
    padding:30px 34px;box-shadow:var(--shadow)}
  .backlink{display:inline-flex;align-items:center;gap:6px;font-size:13px;color:var(--muted);
    cursor:pointer;margin-bottom:16px}
  .backlink:hover{color:var(--accent)}
  .reader-head{border-bottom:1px solid var(--line);padding-bottom:16px;margin-bottom:20px}
  .reader-head h2{margin:0 0 10px;font-size:26px;letter-spacing:-.02em}
  .md{font-size:15px}
  .md h1{font-size:22px;margin:24px 0 12px;letter-spacing:-.01em}
  .md h2{font-size:19px;margin:22px 0 10px;letter-spacing:-.01em}
  .md h3{font-size:16px;margin:18px 0 8px}
  .md p{margin:10px 0}
  .md ul,.md ol{margin:10px 0;padding-left:22px}
  .md li{margin:4px 0}
  .md code{background:var(--surface-2);border:1px solid var(--line);border-radius:6px;
    padding:1px 6px;font-size:13px;font-family:"SF Mono",Menlo,Consolas,monospace}
  .md pre{background:#15172a;color:#e7e9f4;border-radius:12px;padding:16px 18px;overflow:auto;font-size:13px}
  .md pre code{background:none;border:none;color:inherit;padding:0}
  .md blockquote{border-left:3px solid var(--accent);margin:14px 0;padding:4px 16px;
    color:var(--muted);background:var(--surface-2);border-radius:0 10px 10px 0}
  .md hr{border:none;border-top:1px solid var(--line);margin:22px 0}
  .md table{border-collapse:collapse;width:100%;margin:14px 0;font-size:14px}
  .md th,.md td{border:1px solid var(--line);padding:8px 12px;text-align:left;vertical-align:top}
  .md th{background:var(--surface-2);font-weight:600}
  .md tr:nth-child(even) td{background:var(--surface-2)}

  /* ---- Journal timeline ---- */
  .timeline{position:relative;margin-left:8px;padding-left:26px}
  .timeline:before{content:"";position:absolute;left:5px;top:6px;bottom:6px;width:2px;background:var(--line)}
  .tl-item{position:relative;margin-bottom:18px}
  .tl-item:before{content:"";position:absolute;left:-25px;top:5px;width:12px;height:12px;border-radius:50%;
    background:var(--accent);border:3px solid var(--surface);box-shadow:0 0 0 1px var(--line)}
  .tl-item .tl-date{font-size:12px;color:var(--muted);font-weight:600}
  .tl-card{background:var(--surface);border:1px solid var(--line);border-radius:12px;
    padding:12px 16px;box-shadow:var(--shadow);margin-top:6px}
  .tl-card .tl-file{font-size:12px;font-family:"SF Mono",Menlo,Consolas,monospace;color:var(--accent)}
  .tl-card .tl-sum{margin:4px 0 0;font-size:14px}
  .tl-card .tl-auth{font-size:12px;color:var(--muted)}

  /* ---- Search results ---- */
  .hit-snippet{font-size:13px;color:var(--muted);margin-top:6px}
  mark{background:#fff1a8;color:inherit;border-radius:3px;padding:0 2px}
  .empty{text-align:center;color:var(--muted);padding:60px 20px}
  .empty .big{font-size:40px;margin-bottom:10px}

  footer{color:var(--muted);font-size:12px;text-align:center;padding:30px 0 10px}
  .pill{display:inline-block;font-size:11px;background:var(--accent-soft);color:#4a3fc0;
    border-radius:20px;padding:2px 10px;margin-left:8px;font-weight:600}
  .hidden{display:none!important}
  @media (max-width:820px){
    .layout{grid-template-columns:1fr}
    nav.side{position:static;flex-direction:row;flex-wrap:wrap;margin-bottom:8px}
    .navitem .badge{margin-left:6px}
    .search{max-width:none}
  }
</style>
</head>
<body>
<header class="top">
  <div class="top-inner">
    <div class="brand" onclick="go('home')">
      <div class="logo">&#129504;</div>
      <div><h1>Cerveau partage</h1><p>Cockpit &middot; lecture seule</p></div>
    </div>
    <div class="search">
      <span class="si">&#128269;</span>
      <input id="q" type="search" placeholder="Rechercher dans les fiches, mots-cles, journal..." autocomplete="off">
      <kbd>/</kbd>
    </div>
  </div>
</header>

<div class="wrap">
  <div class="layout">
    <nav class="side" id="nav"></nav>
    <main id="main"></main>
  </div>
</div>

<footer>
  Snapshot genere le <span id="genstamp"></span> &middot; page autonome en lecture seule, regeneree avec <code>_cockpit/generate.py</code>.
  <span class="pill">pas d'ecriture sans &laquo;&nbsp;MAJ cerveau&nbsp;&raquo;</span>
  <div style="margin-top:8px">Cerveau partage &middot; cree par <a href="https://www.linkedin.com/in/clementdeschamps/" target="_blank" rel="noopener">Cl&eacute;ment Deschamps</a></div>
</footer>

<script>
const DATA = __DATA__;
const GENERATED = "__GENERATED__";
document.getElementById('genstamp').textContent = GENERATED;

/* ---------- mini Markdown -> HTML (autonome) ---------- */
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function inlineMd(s){
  s = esc(s);
  s = s.replace(/`([^`]+)`/g,'<code>$1</code>');
  s = s.replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2" target="_blank" rel="noopener">$1</a>');
  s = s.replace(/(^|[^\w])(https?:\/\/[^\s<]+)/g, (m,p,u)=> p+'<a href="'+u+'" target="_blank" rel="noopener">'+u+'</a>');
  s = s.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');
  s = s.replace(/(^|[^*])\*([^*\s][^*]*)\*/g,'$1<em>$2</em>');
  return s;
}
function renderMd(src){
  if(!src) return '';
  const lines = src.replace(/\r/g,'').split('\n');
  let html='', i=0;
  function flushTableMaybe(){}
  while(i<lines.length){
    let line = lines[i];
    // table
    if(/^\s*\|.*\|\s*$/.test(line) && i+1<lines.length && /^\s*\|?[\s:|-]+\|?\s*$/.test(lines[i+1]) && lines[i+1].includes('-')){
      const header = line.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim());
      i+=2;
      let rows=[];
      while(i<lines.length && /^\s*\|.*\|\s*$/.test(lines[i])){
        rows.push(lines[i].trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim()));
        i++;
      }
      html+='<table><thead><tr>'+header.map(h=>'<th>'+inlineMd(h)+'</th>').join('')+'</tr></thead><tbody>';
      rows.forEach(r=>{html+='<tr>'+r.map(c=>'<td>'+inlineMd(c)+'</td>').join('')+'</tr>';});
      html+='</tbody></table>';
      continue;
    }
    // code fence
    if(/^```/.test(line)){
      i++; let buf=[];
      while(i<lines.length && !/^```/.test(lines[i])){buf.push(lines[i]);i++;}
      i++;
      html+='<pre><code>'+esc(buf.join('\n'))+'</code></pre>';
      continue;
    }
    // heading
    let h = line.match(/^(#{1,6})\s+(.*)$/);
    if(h){ const lvl=h[1].length; html+='<h'+lvl+'>'+inlineMd(h[2])+'</h'+lvl+'>'; i++; continue; }
    // hr
    if(/^\s*([-*_])\1{2,}\s*$/.test(line)){ html+='<hr>'; i++; continue; }
    // blockquote
    if(/^\s*>\s?/.test(line)){
      let buf=[];
      while(i<lines.length && /^\s*>\s?/.test(lines[i])){buf.push(lines[i].replace(/^\s*>\s?/,''));i++;}
      html+='<blockquote>'+renderMd(buf.join('\n'))+'</blockquote>';
      continue;
    }
    // unordered list
    if(/^\s*[-*]\s+/.test(line)){
      let buf=[];
      while(i<lines.length && /^\s*[-*]\s+/.test(lines[i])){buf.push(lines[i].replace(/^\s*[-*]\s+/,''));i++;}
      html+='<ul>'+buf.map(b=>'<li>'+inlineMd(b)+'</li>').join('')+'</ul>';
      continue;
    }
    // ordered list
    if(/^\s*\d+\.\s+/.test(line)){
      let buf=[];
      while(i<lines.length && /^\s*\d+\.\s+/.test(lines[i])){buf.push(lines[i].replace(/^\s*\d+\.\s+/,''));i++;}
      html+='<ol>'+buf.map(b=>'<li>'+inlineMd(b)+'</li>').join('')+'</ol>';
      continue;
    }
    // blank
    if(/^\s*$/.test(line)){ i++; continue; }
    // paragraph
    let buf=[line]; i++;
    while(i<lines.length && !/^\s*$/.test(lines[i]) && !/^(#{1,6})\s/.test(lines[i])
          && !/^\s*[-*]\s+/.test(lines[i]) && !/^\s*\d+\.\s+/.test(lines[i])
          && !/^\s*>\s?/.test(lines[i]) && !/^```/.test(lines[i])
          && !/^\s*([-*_])\1{2,}\s*$/.test(lines[i])){buf.push(lines[i]);i++;}
    html+='<p>'+inlineMd(buf.join(' '))+'</p>';
  }
  return html;
}

function plainExcerpt(src,n){
  let t = src.replace(/[#>*`\-]/g,' ').replace(/\[([^\]]+)\]\([^)]+\)/g,'$1').replace(/\s+/g,' ').trim();
  return t.length>n ? t.slice(0,n)+'…' : t;
}
function statusClass(s){
  const l=(s||'').toLowerCase();
  if(l.includes('stable')) return 'st-stable';
  if(l.includes('cours')) return 'st-encours';
  return 'st-example';
}
function noteById(fid,file){
  const f = DATA.folders.find(x=>x.id===fid);
  return f ? f.notes.find(n=>n.file===file) : null;
}

/* ---------- navigation ---------- */
let current = {view:'home'};
function buildNav(){
  const nav = document.getElementById('nav');
  let h = '<div class="navlabel">Vue</div>';
  h += navItem('home','&#127968;','Accueil','');
  h += '<div class="navlabel">Dossiers</div>';
  DATA.folders.forEach(f=>{
    const c = f.count_real + f.count_example;
    h += navItem('folder:'+f.id, f.icon, f.label, c? String(c):'0');
  });
  h += '<div class="navlabel">Reperes</div>';
  h += navItem('journal','&#128220;','Journal', String(DATA.journal.length));
  h += navItem('conventions','&#128214;','Conventions','');
  nav.innerHTML = h;
}
function navItem(key,icon,label,badge){
  const act = (routeKey()===key)?' active':'';
  const b = badge!==''? '<span class="badge">'+badge+'</span>':'';
  return '<div class="navitem'+act+'" onclick="go(\''+key+'\')"><span class="ic">'+icon+'</span><span>'+label+'</span>'+b+'</div>';
}
function routeKey(){
  if(current.view==='home') return 'home';
  if(current.view==='folder') return 'folder:'+current.fid;
  if(current.view==='note') return 'folder:'+current.fid;
  if(current.view==='journal') return 'journal';
  if(current.view==='conventions') return 'conventions';
  return '';
}
function go(key){
  document.getElementById('q').value='';
  if(key==='home') current={view:'home'};
  else if(key==='journal') current={view:'journal'};
  else if(key==='conventions') current={view:'conventions'};
  else if(key.startsWith('folder:')) current={view:'folder',fid:key.slice(7)};
  render();
  window.scrollTo({top:0,behavior:'smooth'});
}
function openNote(fid,file){current={view:'note',fid:fid,file:file};render();window.scrollTo({top:0,behavior:'smooth'});}

/* ---------- views ---------- */
function render(){
  buildNav();
  const main = document.getElementById('main');
  if(current.view==='home') main.innerHTML = viewHome();
  else if(current.view==='folder') main.innerHTML = viewFolder(current.fid);
  else if(current.view==='note') main.innerHTML = viewNote(current.fid,current.file);
  else if(current.view==='journal') main.innerHTML = viewJournal();
  else if(current.view==='conventions') main.innerHTML = viewConventions();
}

function viewHome(){
  const s = DATA.stats;
  let h = '<section class="hero"><h2>Le savoir de l\'equipe, d\'un coup d\'oeil</h2>'+
    '<p>Cette page lit le dossier <code>cerveau/</code> et le presente sans jamais le modifier. '+
    'Clique une categorie pour parcourir ses fiches, ou cherche par mot-cle. '+
    'L\'ecriture reste manuelle, declenchee par &laquo;&nbsp;MAJ cerveau&nbsp;&raquo;.</p>'+
    '<div class="stats">'+
      stat(s.notes,'fiches')+
      stat(s.folders+'/'+s.folders_total,'dossiers actifs')+
      stat(s.journal,'entrees au journal')+
      stat(s.last_update||'-','derniere maj')+
    '</div></section>';
  h += '<div class="sectiontitle">Table d\'aiguillage</div>';
  h += '<div class="grid">';
  DATA.folders.forEach(f=>{ h += folderCard(f); });
  h += '</div>';
  if(DATA.journal.length){
    h += '<div class="sectiontitle">Dernieres ecritures</div>';
    h += timelineHtml(DATA.journal.slice(0,4));
    if(DATA.journal.length>4) h += '<p style="margin-top:6px"><a onclick="go(\'journal\')" style="cursor:pointer">Voir tout le journal &rarr;</a></p>';
  }
  return h;
}
function stat(v,l){return '<div class="stat"><b>'+v+'</b><span>'+l+'</span></div>';}
function folderCard(f){
  const real=f.count_real, ex=f.count_example;
  let cnt = real+' fiche'+(real>1?'s':'');
  if(real===0 && ex>0) cnt = ex+' exemple'+(ex>1?'s':'');
  else if(ex>0) cnt += ' + '+ex+' ex.';
  return '<div class="card" onclick="go(\'folder:'+f.id+'\')">'+
    '<span class="count">'+cnt+'</span>'+
    '<div class="topbar" style="background:'+f.accent+'"></div>'+
    '<div class="ic">'+f.icon+'</div>'+
    '<h3>'+f.label+'</h3>'+
    '<p class="sub">'+f.subject+'</p>'+
    '<p class="ex">'+f.examples+'</p>'+
  '</div>';
}
function viewFolder(fid){
  const f = DATA.folders.find(x=>x.id===fid);
  if(!f) return viewHome();
  let h = '<div class="backlink" onclick="go(\'home\')">&larr; Accueil</div>';
  h += '<section class="hero" style="padding:22px 26px"><h2>'+f.icon+' '+f.label+'</h2>'+
    '<p>'+f.subject+'. <span style="opacity:.8">'+f.examples+'</span></p></section>';
  const real = f.notes.filter(n=>!n.is_example);
  const ex = f.notes.filter(n=>n.is_example);
  if(real.length===0 && ex.length===0){
    return h + emptyState('&#128193;','Aucune fiche ici pour le moment.','Range une info avec &laquo; MAJ cerveau &raquo; pour la voir apparaitre.');
  }
  if(real.length){ h += '<div class="sectiontitle">Fiches</div>'; real.forEach(n=>{h+=noteCard(f.id,n);}); }
  if(ex.length){ h += '<div class="sectiontitle">Exemples (a remplacer ou supprimer)</div>'; ex.forEach(n=>{h+=noteCard(f.id,n);}); }
  return h;
}
function noteCard(fid,n){
  const stcls = n.is_example?'st-example':statusClass(n.statut);
  const stlabel = n.is_example?'exemple':(n.statut||'fiche');
  let meta = '<span class="badge-status '+stcls+'">'+stlabel+'</span>';
  if(n.maj) meta += '<span class="chip">&#128197; '+n.maj+'</span>';
  if(n.auteur) meta += '<span class="chip">'+n.auteur+'</span>';
  const kws = (n.motscles||[]).slice(0,4).map(k=>'<span class="chip kw">'+k+'</span>').join('');
  return '<div class="notecard" onclick="openNote(\''+fid+'\',\''+n.file.replace(/'/g,"\\'")+'\')">'+
    '<h3>'+n.title+'</h3>'+
    '<div class="notemeta">'+meta+kws+'</div>'+
    '<p class="excerpt">'+plainExcerpt(n.body,160)+'</p>'+
  '</div>';
}
function viewNote(fid,file){
  const f = DATA.folders.find(x=>x.id===fid);
  const n = noteById(fid,file);
  if(!n) return viewHome();
  const stcls = n.is_example?'st-example':statusClass(n.statut);
  const stlabel = n.is_example?'exemple':(n.statut||'fiche');
  let meta = '<span class="badge-status '+stcls+'">'+stlabel+'</span>';
  if(n.maj) meta += '<span class="chip">&#128197; maj '+n.maj+'</span>';
  if(n.auteur) meta += '<span class="chip">&#9999;&#65039; '+n.auteur+'</span>';
  meta += '<span class="chip">'+f.icon+' '+f.label+'</span>';
  const kws = (n.motscles||[]).map(k=>'<span class="chip kw">'+k+'</span>').join('');
  return '<div class="backlink" onclick="go(\'folder:'+fid+'\')">&larr; '+f.label+'</div>'+
    '<article class="reader">'+
      '<div class="reader-head"><h2>'+n.title+'</h2>'+
      '<div class="notemeta">'+meta+kws+'</div></div>'+
      '<div class="md">'+renderMd(n.body)+'</div>'+
      '<p style="margin-top:24px;font-size:12px;color:var(--muted)">Fichier&nbsp;: <code>'+fid+'/'+n.file+'</code></p>'+
    '</article>';
}
function viewJournal(){
  let h = '<div class="backlink" onclick="go(\'home\')">&larr; Accueil</div>';
  h += '<section class="hero" style="padding:22px 26px"><h2>&#128220; Journal des ecritures</h2>'+
    '<p>Trace auditable de chaque ajout au cerveau, la plus recente en haut.</p></section>';
  if(!DATA.journal.length) return h + emptyState('&#128220;','Journal vide.','');
  return h + timelineHtml(DATA.journal);
}
function timelineHtml(rows){
  let h='<div class="timeline">';
  rows.forEach(r=>{
    h+='<div class="tl-item"><div class="tl-date">'+r.date+'</div>'+
      '<div class="tl-card"><span class="tl-file">'+inlineMd(r.fichier)+'</span>'+
      '<p class="tl-sum">'+inlineMd(r.resume)+'</p>'+
      '<span class="tl-auth">par '+r.auteur+'</span></div></div>';
  });
  return h+'</div>';
}
function viewConventions(){
  let h = '<div class="backlink" onclick="go(\'home\')">&larr; Accueil</div>';
  h += '<article class="reader"><div class="md">'+renderMd(DATA.contexte)+'</div></article>';
  return h;
}
function emptyState(ic,t,s){
  return '<div class="empty"><div class="big">'+ic+'</div><div style="font-size:16px;color:var(--ink)">'+t+'</div>'+(s?'<p>'+s+'</p>':'')+'</div>';
}

/* ---------- search ---------- */
function hilite(text,q){
  const lc=text.toLowerCase(), idx=lc.indexOf(q.toLowerCase());
  if(idx<0) return esc(text.slice(0,160));
  const start=Math.max(0,idx-50);
  const pre=(start>0?String.fromCharCode(8230):"")+text.slice(start,idx);
  const mid=text.slice(idx,idx+q.length);
  const post=text.slice(idx+q.length, idx+q.length+90)+String.fromCharCode(8230);
  return esc(pre)+"<mark>"+esc(mid)+"</mark>"+esc(post);
}
function doSearch(q){
  q=q.trim();
  const main=document.getElementById('main');
  if(q.length<2){ render(); return; }
  buildNav();
  const ql=q.toLowerCase();
  let hits=[];
  DATA.folders.forEach(f=>{
    f.notes.forEach(n=>{
      const hay=(n.title+' '+(n.motscles||[]).join(' ')+' '+n.body).toLowerCase();
      if(hay.includes(ql)){
        let where = n.title.toLowerCase().includes(ql)?'titre':
          ((n.motscles||[]).join(' ').toLowerCase().includes(ql)?'mot-cle':'contenu');
        hits.push({f:f,n:n,where:where});
      }
    });
  });
  let jh=[];
  DATA.journal.forEach(r=>{
    if((r.resume+' '+r.fichier+' '+r.auteur).toLowerCase().includes(ql)) jh.push(r);
  });
  let h='<section class="hero" style="padding:20px 24px"><h2>Recherche : &laquo; '+esc(q)+' &raquo;</h2>'+
    '<p>'+hits.length+' fiche(s) et '+jh.length+' entree(s) de journal correspondent.</p></section>';
  if(!hits.length && !jh.length){
    main.innerHTML = h + emptyState('&#128269;','Rien trouve.','Essaie un autre terme ou parcours les dossiers.');
    return;
  }
  if(hits.length){
    h+='<div class="sectiontitle">Fiches</div>';
    hits.forEach(hit=>{
      const n=hit.n,f=hit.f;
      h+='<div class="notecard" onclick="openNote(\''+f.id+'\',\''+n.file.replace(/'/g,"\\'")+'\')">'+
        '<h3>'+n.title+'</h3>'+
        '<div class="notemeta"><span class="chip">'+f.icon+' '+f.label+'</span>'+
        '<span class="chip kw">trouve dans : '+hit.where+'</span></div>'+
        '<p class="hit-snippet">'+hilite(n.body||n.title, q)+'</p></div>';
    });
  }
  if(jh.length){
    h+='<div class="sectiontitle">Journal</div>'+timelineHtml(jh);
  }
  main.innerHTML=h;
}

/* ---------- events ---------- */
const qinput=document.getElementById('q');
qinput.addEventListener('input',e=>doSearch(e.target.value));
document.addEventListener('keydown',e=>{
  if(e.key==='/' && document.activeElement!==qinput){e.preventDefault();qinput.focus();}
  if(e.key==='Escape'){qinput.value='';render();qinput.blur();}
});

render();
</script>
</body>
</html>
"""


def main():
    if len(sys.argv) > 1:
        root = os.path.abspath(sys.argv[1])
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        root = os.path.dirname(here)  # parent de _cockpit/

    if not os.path.isfile(os.path.join(root, "00_CONTEXTE.md")):
        print("ERREUR : dossier cerveau introuvable (pas de 00_CONTEXTE.md) ->", root)
        sys.exit(1)

    data = build_data(root)
    generated = datetime.datetime.now().strftime("%d/%m/%Y a %Hh%M")
    html = HTML_TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False))
    html = html.replace("__GENERATED__", generated)

    out = os.path.join(root, "cockpit.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

    s = data["stats"]
    print("OK -> " + out)
    print("Fiches: %d | Exemples: %d | Dossiers actifs: %d/%d | Journal: %d | Derniere maj: %s"
          % (s["notes"], s["examples"], s["folders"], s["folders_total"], s["journal"], s["last_update"]))


if __name__ == "__main__":
    main()
