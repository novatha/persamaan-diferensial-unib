# -*- coding: utf-8 -*-

# 1. silabus.astro
silabus_content = """---
import Layout from '../layouts/Layout.astro';
import { pdMetadata, pdModules } from '../data/pdData';

const base = import.meta.env.BASE_URL.endsWith('/')
  ? import.meta.env.BASE_URL.slice(0, -1)
  : import.meta.env.BASE_URL;

const getUrl = (path: string) => `${base}${path}`;
---

<Layout title="Silabus & Rencana Pembelajaran Semester (RPS) | Persamaan Diferensial UNIB 2026" description="Kurikulum & Rencana Pembelajaran Semester Berbasis OBE S1 Teknik Elektro Universitas Bengkulu.">
  <!-- Header Banner -->
  <section class="silabus-header">
    <div class="container">
      <div class="header-breadcrumbs">
        <a href={getUrl('/')} class="crumb-link">&larr; Kembali ke Beranda</a>
        <span class="crumb-sep">/</span>
        <span class="crumb-current">Silabus &amp; Rencana Pembelajaran</span>
      </div>

      <div class="header-content">
        <span class="pill-badge">
          <i data-lucide="graduation-cap"></i> KURIKULUM OBE BERBASIS SN-DIKTI
        </span>
        <h1 class="header-title">
          Silabus &amp; Rencana Pembelajaran <span class="gradient-text">Semester (RPS)</span>
        </h1>
        <p class="header-lead">
          Struktur kurikulum mata kuliah Persamaan Diferensial (TEE-203) S1 Teknik Elektro UNIB dengan penekanan pada integrasi 4-Pilar Pedagogis: Intuisi Fisika, Derivasi Matematis Eksplisit, Komputasi Numerik Terbuka, dan Aplikasi Rekayasa Elektro.
        </p>
      </div>
    </div>
  </section>

  <section class="silabus-body">
    <div class="container">
      <!-- Unduh Dokumen Resmi RPS -->
      <div class="glass-panel rps-download-panel">
        <div class="rps-meta-flex">
          <div class="rps-icon-box">
            <i data-lucide="file-check-2"></i>
          </div>
          <div>
            <h3 class="rps-panel-title">Dokumen Resmi RPS Persamaan Diferensial 2026</h3>
            <p class="rps-panel-desc">Dokumen kurikulum lengkap memuat matriks pemetaan CPL-CPMK-SubCPMK, rubrik penilaian portofolio OBE, dan jadwal perkuliahan 16 minggu.</p>
          </div>
        </div>
        <a href={getUrl('/pdf/RPS_Persamaan_Diferensial.pdf')} target="_blank" rel="noopener noreferrer" class="btn btn-primary">
          <i data-lucide="download"></i> Unduh RPS Lengkap (PDF)
        </a>
      </div>

      <!-- Tabel Matriks 16 Minggu -->
      <div class="glass-panel table-panel">
        <h2 class="panel-section-title">
          <i data-lucide="calendar"></i> Matriks Perkuliahan Mingguan (16 Minggu)
        </h2>
        <div class="table-responsive">
          <table class="silabus-table">
            <thead>
              <tr>
                <th>Mg</th>
                <th>Sub-CPMK &amp; Topik Materi</th>
                <th>Fokus Teori &amp; Derivasi</th>
                <th>Praktikum Komputasi Terbuka</th>
                <th>Bahan Ajar</th>
              </tr>
            </thead>
            <tbody>
              {pdModules.map((m) => (
                <tr>
                  <td class="week-cell"><strong>W{m.week}</strong></td>
                  <td>
                    <strong>{m.title}</strong><br />
                    <span class="subcpmk-text">{m.subCpmk}</span>
                  </td>
                  <td>
                    <ul class="topic-bullet-list">
                      {m.theoryTopics.map((t) => (<li>{t}</li>))}
                    </ul>
                  </td>
                  <td>
                    <span class="lab-tag">{m.computationLab}</span>
                  </td>
                  <td>
                    <a href={getUrl(m.slidesPdf)} class="doc-link-btn" title="Slide PDF">
                      <i data-lucide="presentation"></i> Slide
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
</Layout>

<style>
  .silabus-header {
    padding: 60px 0 40px;
    background: radial-gradient(circle at 50% 0%, rgba(245, 158, 11, 0.08) 0%, transparent 60%);
    border-bottom: 1px solid var(--border-subtle);
  }
  .header-breadcrumbs { display: flex; align-items: center; gap: 8px; margin-bottom: 18px; font-size: 0.85rem; }
  .crumb-link { color: var(--neon-gold); text-decoration: none; font-weight: 600; }
  .crumb-link:hover { text-decoration: underline; }
  .crumb-sep { color: var(--text-dim); }
  .crumb-current { color: var(--text-muted); }
  .header-title { font-size: 2.4rem; font-weight: 800; margin: 14px 0 12px; line-height: 1.2; }
  .header-lead { font-size: 1rem; color: var(--text-muted); max-width: 740px; line-height: 1.6; }
  .silabus-body { padding: 50px 0 80px; }
  .rps-download-panel {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 24px 28px;
    border-radius: var(--radius-lg);
    margin-bottom: 36px;
    flex-wrap: wrap;
    gap: 20px;
  }
  .rps-meta-flex { display: flex; align-items: center; gap: 20px; max-width: 700px; }
  .rps-icon-box {
    width: 52px;
    height: 52px;
    background: rgba(245, 158, 11, 0.15);
    border: 1px solid rgba(245, 158, 11, 0.3);
    border-radius: var(--radius-md);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--neon-gold);
    flex-shrink: 0;
  }
  .rps-panel-title { font-size: 1.15rem; font-weight: 800; margin: 0 0 4px; color: var(--text-main); }
  .rps-panel-desc { font-size: 0.88rem; color: var(--text-muted); margin: 0; line-height: 1.5; }
  .table-panel { padding: 28px; border-radius: var(--radius-lg); }
  .panel-section-title { font-size: 1.35rem; font-weight: 800; margin: 0 0 24px; display: flex; align-items: center; gap: 10px; }
  .table-responsive { overflow-x: auto; }
  .silabus-table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
  .silabus-table th {
    background: rgba(255, 255, 255, 0.04);
    padding: 12px 14px;
    text-align: left;
    color: var(--text-main);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  }
  .silabus-table td {
    padding: 14px 14px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    vertical-align: top;
    color: var(--text-muted);
  }
  .week-cell { color: var(--neon-gold); font-size: 1rem; }
  .subcpmk-text { font-size: 0.78rem; color: var(--text-dim); display: inline-block; margin-top: 4px; }
  .topic-bullet-list { margin: 0; padding-left: 18px; font-size: 0.82rem; line-height: 1.5; }
  .lab-tag {
    display: inline-block;
    font-size: 0.76rem;
    color: var(--neon-cyan);
    background: rgba(6, 182, 212, 0.1);
    border: 1px solid rgba(6, 182, 212, 0.2);
    padding: 4px 8px;
    border-radius: 4px;
  }
  .doc-link-btn {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 0.76rem;
    font-weight: 600;
    color: var(--neon-gold);
    background: rgba(245, 158, 11, 0.1);
    border: 1px solid rgba(245, 158, 11, 0.2);
    padding: 4px 10px;
    border-radius: 4px;
    text-decoration: none;
  }
  .doc-link-btn:hover { background: var(--neon-gold); color: #04121e; }
</style>
"""

with open("portal/src/pages/silabus.astro", "w") as f:
    f.write(silabus_content)

# 2. tugas.astro
tugas_content = """---
import Layout from '../layouts/Layout.astro';
import { pdModules } from '../data/pdData';

const base = import.meta.env.BASE_URL.endsWith('/')
  ? import.meta.env.BASE_URL.slice(0, -1)
  : import.meta.env.BASE_URL;

const getUrl = (path?: string) => path ? `${base}${path}` : null;
---

<Layout title="Solved Problems & Problem Sets (C1–C6) | Persamaan Diferensial UNIB 2026" description="Kumpulan Latihan Soal dan Pembahasan Lengkap Solved Problems Level Bloom C1-C6 Persamaan Diferensial.">
  <section class="tugas-header">
    <div class="container">
      <div class="header-breadcrumbs">
        <a href={getUrl('/')} class="crumb-link">&larr; Kembali ke Beranda</a>
        <span class="crumb-sep">/</span>
        <span class="crumb-current">Solved Problems &amp; Bank Soal</span>
      </div>

      <div class="header-content">
        <span class="pill-badge">
          <i data-lucide="check-square"></i> BANK SOAL TERSTRUKTUR C1–C6
        </span>
        <h1 class="header-title">
          Koleksi <span class="gradient-text">Solved Problems &amp; Worksheet</span>
        </h1>
        <p class="header-lead">
          Akses seluruh Lembar Kerja Mahasiswa (LKM) dan Problem Set mingguan yang dirancang berjenjang dari level mengingat (C1), memahami (C2), menerapkan analitis (C3), menganalisis sistem (C4), mengevaluasi batas operasional (C5), hingga merancang komputasi terbuka (C6).
        </p>
      </div>
    </div>
  </section>

  <section class="tugas-body">
    <div class="container">
      <div class="tugas-grid">
        {pdModules.map((m) => (
          <div class="glass-panel tugas-card">
            <div class="tugas-card-header">
              <span class="week-pill">Minggu {m.week}</span>
              <h3 class="tugas-card-title">{m.title}</h3>
            </div>
            
            <p class="tugas-card-sub">{m.subTitle}</p>

            <div class="bloom-box">
              <span class="bloom-label">Fokus Asesmen Taksonomi Bloom:</span>
              <ul class="bloom-list">
                <li><strong>C1–C2:</strong> {m.bloomHighlights.c1_c2}</li>
                <li><strong>C3–C4:</strong> {m.bloomHighlights.c3_c4}</li>
                <li><strong>C5–C6:</strong> {m.bloomHighlights.c5_c6}</li>
              </ul>
            </div>

            <div class="tugas-action-row">
              {m.worksheetPdf && (
                <a href={getUrl(m.worksheetPdf)} target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-cyan">
                  <i data-lucide="file-text"></i> Lembar Kerja
                </a>
              )}
              {m.solvedPdf && (
                <a href={getUrl(m.solvedPdf)} target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline">
                  <i data-lucide="check-circle"></i> Solved Problems
                </a>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>
</Layout>

<style>
  .tugas-header {
    padding: 60px 0 40px;
    background: radial-gradient(circle at 50% 0%, rgba(16, 185, 129, 0.08) 0%, transparent 60%);
    border-bottom: 1px solid var(--border-subtle);
  }
  .header-breadcrumbs { display: flex; align-items: center; gap: 8px; margin-bottom: 18px; font-size: 0.85rem; }
  .crumb-link { color: var(--neon-emerald); text-decoration: none; font-weight: 600; }
  .crumb-link:hover { text-decoration: underline; }
  .crumb-sep { color: var(--text-dim); }
  .crumb-current { color: var(--text-muted); }
  .header-title { font-size: 2.4rem; font-weight: 800; margin: 14px 0 12px; line-height: 1.2; }
  .header-lead { font-size: 1rem; color: var(--text-muted); max-width: 740px; line-height: 1.6; }
  .tugas-body { padding: 50px 0 80px; }
  .tugas-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 24px;
  }
  .tugas-card {
    padding: 24px;
    border-radius: var(--radius-lg);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .week-pill {
    font-size: 0.75rem;
    font-weight: 800;
    color: var(--neon-emerald);
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.25);
    padding: 3px 10px;
    border-radius: var(--radius-pill);
    display: inline-block;
    margin-bottom: 8px;
  }
  .tugas-card-title { font-size: 1.15rem; font-weight: 800; margin: 0 0 6px; color: var(--text-main); }
  .tugas-card-sub { font-size: 0.82rem; color: var(--text-dim); margin-bottom: 16px; line-height: 1.4; }
  .bloom-box {
    background: rgba(9, 13, 22, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: var(--radius-sm);
    padding: 12px;
    margin-bottom: 18px;
  }
  .bloom-label { font-size: 0.7rem; text-transform: uppercase; font-weight: 700; color: var(--neon-emerald); display: block; margin-bottom: 6px; }
  .bloom-list { list-style: none; padding: 0; margin: 0; font-size: 0.76rem; color: var(--text-muted); display: flex; flex-direction: column; gap: 4px; }
  .tugas-action-row { display: flex; gap: 10px; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 14px; }
</style>
"""

with open("portal/src/pages/tugas.astro", "w") as f:
    f.write(tugas_content)

# 3. ujian.astro
ujian_content = """---
import Layout from '../layouts/Layout.astro';

const base = import.meta.env.BASE_URL.endsWith('/')
  ? import.meta.env.BASE_URL.slice(0, -1)
  : import.meta.env.BASE_URL;

const getUrl = (path: string) => `${base}${path}`;
---

<Layout title="Informasi & Arsip UTS/UAS | Persamaan Diferensial UNIB 2026" description="Ketentuan, Format Asesmen, dan Arsip Soal Ujian Tengah Semester & Ujian Akhir Semester Persamaan Diferensial.">
  <section class="ujian-header">
    <div class="container">
      <div class="header-breadcrumbs">
        <a href={getUrl('/')} class="crumb-link">&larr; Kembali ke Beranda</a>
        <span class="crumb-sep">/</span>
        <span class="crumb-current">Evaluasi Tengah &amp; Akhir Semester</span>
      </div>

      <div class="header-content">
        <span class="pill-badge">
          <i data-lucide="target"></i> EVALUASI KINERJA PEMBELAJARAN
        </span>
        <h1 class="header-title">
          Arsip Ujian &amp; <span class="gradient-text">Solusi Resmi UTS / UAS</span>
        </h1>
        <p class="header-lead">
          Pusat unduhan naskah soal resmi dan pembahasan analitis langkah demi langkah Ujian Tengah Semester (UTS) dan Ujian Akhir Semester (UAS) mata kuliah Persamaan Diferensial.
        </p>
      </div>
    </div>
  </section>

  <section class="ujian-body">
    <div class="container">
      <div class="grid-2col">
        <!-- Card UTS -->
        <div class="glass-panel exam-card">
          <div class="exam-header-row">
            <span class="exam-pill">EVALUASI MINGGU 8</span>
            <span class="exam-badge">Bobot 25%</span>
          </div>
          <h2 class="exam-title">Ujian Tengah Semester (UTS)</h2>
          <p class="exam-desc">Mencakup Capaian Pembelajaran CPMK-1 s.d. CPMK-4: Klasifikasi PDB, PDB Orde 1 Separabel &amp; Eksak, Transien RC &amp; RL, PDB Orde 2 Homogen LC, RLC Seri Sinusoidal, dan Transformasi Laplace.</p>
          
          <div class="exam-actions">
            <a href={getUrl('/pdf/uts.pdf')} target="_blank" rel="noopener noreferrer" class="btn btn-primary">
              <i data-lucide="file-text"></i> Unduh Soal UTS (PDF)
            </a>
            <a href={getUrl('/pdf/solusi_uts.pdf')} target="_blank" rel="noopener noreferrer" class="btn btn-outline">
              <i data-lucide="check-circle-2"></i> Solusi Lengkap UTS (PDF)
            </a>
          </div>
        </div>

        <!-- Card UAS -->
        <div class="glass-panel exam-card">
          <div class="exam-header-row">
            <span class="exam-pill exam-pill-green">EVALUASI MINGGU 16</span>
            <span class="exam-badge">Bobot 30%</span>
          </div>
          <h2 class="exam-title">Ujian Akhir Semester (UAS)</h2>
          <p class="exam-desc">Mencakup Capaian Pembelajaran CPMK-5 dan CPMK-6: Persamaan Diferensial Parsial (PDP), Deret Fourier Harmonisa, Pemisahan Variabel, Telegrafer Saluran Transmisi 1D, Difusi Panas Kabel, Potensial Laplace 2D, Fungsi Bessel, dan 4 Persamaan Maxwell.</p>
          
          <div class="exam-actions">
            <a href={getUrl('/pdf/uas.pdf')} target="_blank" rel="noopener noreferrer" class="btn btn-cyan">
              <i data-lucide="file-text"></i> Unduh Soal UAS (PDF)
            </a>
            <a href={getUrl('/pdf/solusi_uas.pdf')} target="_blank" rel="noopener noreferrer" class="btn btn-outline">
              <i data-lucide="check-circle-2"></i> Solusi Lengkap UAS (PDF)
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</Layout>

<style>
  .ujian-header {
    padding: 60px 0 40px;
    background: radial-gradient(circle at 50% 0%, rgba(6, 182, 212, 0.08) 0%, transparent 60%);
    border-bottom: 1px solid var(--border-subtle);
  }
  .header-breadcrumbs { display: flex; align-items: center; gap: 8px; margin-bottom: 18px; font-size: 0.85rem; }
  .crumb-link { color: var(--neon-cyan); text-decoration: none; font-weight: 600; }
  .crumb-link:hover { text-decoration: underline; }
  .crumb-sep { color: var(--text-dim); }
  .crumb-current { color: var(--text-muted); }
  .header-title { font-size: 2.4rem; font-weight: 800; margin: 14px 0 12px; line-height: 1.2; }
  .header-lead { font-size: 1rem; color: var(--text-muted); max-width: 740px; line-height: 1.6; }
  .ujian-body { padding: 50px 0 80px; }
  .grid-2col { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
  @media (max-width: 768px) { .grid-2col { grid-template-columns: 1fr; } }
  .exam-card { padding: 32px; border-radius: var(--radius-lg); display: flex; flex-direction: column; justify-content: space-between; }
  .exam-header-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; }
  .exam-pill {
    font-size: 0.75rem;
    font-weight: 800;
    color: var(--neon-gold);
    background: rgba(245, 158, 11, 0.12);
    border: 1px solid rgba(245, 158, 11, 0.25);
    padding: 3px 10px;
    border-radius: var(--radius-pill);
  }
  .exam-pill-green {
    color: var(--neon-cyan);
    background: rgba(6, 182, 212, 0.12);
    border-color: rgba(6, 182, 212, 0.25);
  }
  .exam-badge {
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--text-muted);
    background: rgba(255, 255, 255, 0.05);
    padding: 3px 8px;
    border-radius: var(--radius-pill);
  }
  .exam-title { font-size: 1.5rem; font-weight: 800; margin: 0 0 10px; color: var(--text-main); }
  .exam-desc { font-size: 0.9rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 24px; }
  .exam-actions { display: flex; gap: 12px; flex-wrap: wrap; }
</style>
"""

with open("portal/src/pages/ujian.astro", "w") as f:
    f.write(ujian_content)

print("silabus.astro, tugas.astro, ujian.astro generated successfully!")
