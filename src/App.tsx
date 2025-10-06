import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import './App.css';

function App() {
  const { t, i18n } = useTranslation();
  const [lang, setLang] = useState('en');

  const changeLanguage = (lng: string) => {
    i18n.changeLanguage(lng);
    setLang(lng);
  };

  // Load the list of resume items as objects
  const resumeItems = t('resume.items', { returnObjects: true }) as {
    description: string;
    skills: string[];
    company?: string;
    location?: string;
    date: string;
    image?: string;
    text: string;
  }[];

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

        <h2>{t('sections.professionalSummary')}</h2>

        <section className="resume">
          {resumeItems.map((item, index) => (
            <div className="event" key={index}>
              <div className="graphic">
                <h3>{item.date}</h3>

                {item.image && (
                  <div className="boxImg">
                    <img src={item.image} alt={item.company || `event-${index}`} />
                  </div>
                )}
              </div>

              <div className="details">
                {item.company && <h4 className="font-semibold text-lg">{item.company}</h4>}
                {item.location && <p className="text-sm text-gray-500 italic">{item.location}</p>}

                <p className="mt-2">{item.description}</p>

                {item.skills && item.skills.length > 0 && (
                  <div className="flex flex-wrap gap-2 mt-3">
                    {item.skills.map((skill, i) => (
                      <span
                        key={i}
                        className="px-2 py-1 bg-gray-100 text-gray-700 text-sm rounded-full border hover:bg-gray-200 transition"
                      >
                        {skill}
                      </span>
                    ))}
                  </div>
                )}
              </div>
            </div>
          ))}
        </section>


      </div>
    </main>
  );
}

export default App;
