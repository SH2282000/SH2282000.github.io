import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import './App.css';
import Resume from './resume';
import Education from './education';

function App() {
  const { t, i18n } = useTranslation();
  const [lang, setLang] = useState('en');

  const changeLanguage = (lng: string) => {
    i18n.changeLanguage(lng);
    setLang(lng);
  };

  return (
    <main>
      <header>
        <div className="flags">
          {['de', 'fr', 'en'].map((lng) => (
            <button
              key={lng}
              onClick={() => changeLanguage(lng)}
              style={{ opacity: lang === lng ? 1 : 0.5 }}
            >
              {lng === 'de' ? '🇩🇪' : lng === 'fr' ? '🇫🇷' : '🇺🇸'}
            </button>
          ))}
        </div>
        <h1>{t('header.name')}</h1>
        <p>{t('header.description')}</p>
      </header>

      <div className="content">

        <h2>BLOG</h2>
        <a href="https://SH2282000.github.io/blog" className="resume">
          {t('sections.blog')}
        </a>

        <hr className="section-divider" />
        <Resume />
        <hr className="section-divider" />
        <Education/>


      </div>
    </main>
  );
}

export default App;
