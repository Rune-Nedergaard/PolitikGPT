import React from 'react';
import { Button } from './ui/button';
import { SidebarTrigger } from './ui/sidebar';
import { MoonIcon, SunIcon, Languages } from 'lucide-react';
import { useTheme } from '../hooks/use-theme';
import { useAppContext } from '../context/AppContext';
import { Bot } from 'lucide-react';
const AppHeader = () => {
  const {
    theme,
    setTheme
  } = useTheme();
  const {
    language,
    toggleLanguage
  } = useAppContext();
  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };
  return <header className="border-b border-danish-blue-100 bg-white dark:bg-danish-gray-900 dark:border-danish-gray-800">
      <div className="flex items-center justify-between px-4 py-3 lg:px-8 max-w-7xl mx-auto">
        <div className="flex items-center space-x-4">
          <SidebarTrigger className="md:hidden" />
          <div className="flex items-center">
            <Bot className="h-6 w-6 text-danish-blue mr-2" />
          </div>
          <p className="text-danish-blue-600 font-dstext pl-2 md:pl-0 text-left mx-[200px] text-lg font-medium">
            {language === 'en' ? 'Danish Statistics Explorer' : 'Dansk Statistik Udforsker'}
          </p>
        </div>
        <div className="flex items-center space-x-2">
          <Button variant="ghost" size="icon" className="rounded-full h-8 w-8" onClick={toggleLanguage} title={language === 'en' ? 'Switch to Danish' : 'Switch to English'}>
            <Languages className="h-4 w-4" />
          </Button>
          <Button variant="ghost" size="icon" className="rounded-full h-8 w-8" onClick={toggleTheme} title={theme === 'light' ? 'Switch to dark mode' : 'Switch to light mode'}>
            {theme === 'light' ? <MoonIcon className="h-4 w-4" /> : <SunIcon className="h-4 w-4" />}
          </Button>
        </div>
      </div>
    </header>;
};
export default AppHeader;