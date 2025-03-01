
import React from 'react';
import { AppProvider } from '@/context/AppContext';
import { ThemeProvider } from '@/hooks/use-theme';
import AppHeader from '@/components/AppHeader';
import MessageList from '@/components/MessageList';
import MessageInput from '@/components/MessageInput';
import { SidebarProvider, Sidebar, SidebarContent, SidebarGroup, SidebarHeader } from '@/components/ui/sidebar';
import { Download, BarChart, RefreshCcw, Bot } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { useAppContext } from '@/context/AppContext';

const ActionButtons = () => {
  const { language, clearMessages } = useAppContext();
  
  return (
    <div className="fixed bottom-8 right-8 flex flex-col space-y-2">
      <Button 
        className="rounded-full w-12 h-12 bg-danish-blue shadow-lg hover:bg-danish-blue-600 transition-all duration-300"
        title={language === 'en' ? 'Export data' : 'Eksportér data'}
      >
        <Download className="h-5 w-5" />
      </Button>
      <Button 
        className="rounded-full w-12 h-12 bg-danish-blue shadow-lg hover:bg-danish-blue-600 transition-all duration-300"
        title={language === 'en' ? 'New query' : 'Ny forespørgsel'}
        onClick={clearMessages}
      >
        <RefreshCcw className="h-5 w-5" />
      </Button>
    </div>
  );
};

const ExplorerSidebar = () => {
  const { language } = useAppContext();
  
  return (
    <Sidebar className="max-w-[240px] w-[240px]">
      <SidebarHeader>
        <div className="flex items-center space-x-2 p-4">
          <Bot className="h-6 w-6 text-danish-blue" />
          <span className="font-medium text-danish-blue">
            {language === 'en' ? 'Statistics Explorer' : 'Statistik Udforsker'}
          </span>
        </div>
      </SidebarHeader>
      <SidebarContent>
        <SidebarGroup>
          <h3 className="px-4 text-xs uppercase tracking-wider text-danish-blue-600 font-semibold mb-2">
            {language === 'en' ? 'Recent Queries' : 'Seneste forespørgsler'}
          </h3>
          <div className="space-y-1 px-2">
            {[1, 2, 3].map((i) => (
              <div key={i} className="px-2 py-1.5 text-sm rounded-md hover:bg-danish-blue-50 cursor-pointer transition-colors text-danish-blue-700">
                {language === 'en' ? `Example query ${i}` : `Eksempel forespørgsel ${i}`}
              </div>
            ))}
          </div>
        </SidebarGroup>
        <SidebarGroup>
          <h3 className="px-4 text-xs uppercase tracking-wider text-danish-blue-600 font-semibold mb-2 mt-6">
            {language === 'en' ? 'Data Categories' : 'Datakategorier'}
          </h3>
          <div className="space-y-1 px-2">
            {['Demographics', 'Economy', 'Education', 'Health', 'Environment'].map((category) => (
              <div key={category} className="px-2 py-1.5 text-sm rounded-md hover:bg-danish-blue-50 cursor-pointer transition-colors text-danish-blue-700 flex items-center">
                <BarChart className="h-3.5 w-3.5 mr-2 text-danish-blue-500" />
                <span>
                  {language === 'en' 
                    ? category 
                    : category === 'Demographics' ? 'Demografi' 
                    : category === 'Economy' ? 'Økonomi' 
                    : category === 'Education' ? 'Uddannelse' 
                    : category === 'Health' ? 'Sundhed' 
                    : 'Miljø'}
                </span>
              </div>
            ))}
          </div>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  );
};

const Index = () => {
  return (
    <ThemeProvider defaultTheme="light">
      <AppProvider>
        <SidebarProvider>
          <div className="flex flex-col min-h-screen bg-white w-full">
            <AppHeader />
            <div className="flex flex-1 overflow-hidden">
              <ExplorerSidebar />
              <main className="flex-1 overflow-hidden flex flex-col w-full mx-auto px-4 lg:px-8 max-w-7xl">
                <div className="py-6 flex-1 overflow-hidden flex flex-col">
                  <MessageList />
                </div>
                <div className="pb-6">
                  <MessageInput />
                </div>
                <ActionButtons />
              </main>
            </div>
            <footer className="bg-danish-blue-50 py-3 border-t border-danish-blue-100">
              <div className="max-w-7xl mx-auto px-4 lg:px-8 text-sm text-danish-blue-600">
                <p>© {new Date().getFullYear()} Danish Statistics Explorer</p>
              </div>
            </footer>
          </div>
        </SidebarProvider>
      </AppProvider>
    </ThemeProvider>
  );
};

export default Index;
