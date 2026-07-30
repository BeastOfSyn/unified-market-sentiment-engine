import React from 'react'
import { QueryClient, QueryClientProvider, useQuery } from '@tanstack/react-query'
import { Activity, ShieldCheck, Database, Layers, Radio } from 'lucide-react'

const queryClient = new QueryClient()

function HealthStatus() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['health'],
    queryFn: async () => {
      const res = await fetch('/api/health')
      if (!res.ok) throw new Error('API server returned error')
      return res.json()
    }
  })

  if (isLoading) return <span className="text-slate-400">Pinging backend...</span>
  if (error) return <span className="text-rose-500 font-medium">Offline</span>
  return (
    <span className="text-emerald-400 font-medium flex items-center gap-1.5">
      <ShieldCheck className="w-4 h-4" /> Connected ({data?.status || 'ok'})
    </span>
  )
}

function Dashboard() {
  return (
    <div className="max-w-6xl mx-auto p-6 md:p-12 space-y-12">
      {/* Header */}
      <header className="flex flex-col md:flex-row md:items-center justify-between gap-6 pb-8 border-b border-slate-800">
        <div>
          <div className="flex items-center gap-3">
            <div className="bg-gradient-to-tr from-blue-600 to-indigo-600 p-2 rounded-xl shadow-lg shadow-indigo-500/20">
              <Layers className="w-8 h-8 text-white" />
            </div>
            <h1 className="text-3xl font-extrabold tracking-tight bg-gradient-to-r from-white via-slate-100 to-slate-400 bg-clip-text text-transparent">
              InsightBridge
            </h1>
          </div>
          <p className="text-slate-400 mt-2 text-sm md:text-base">
            Unified Business Intelligence Sentiment Analysis Pipeline
          </p>
        </div>
        <div className="bg-slate-900 border border-slate-800/80 px-4 py-2.5 rounded-2xl flex items-center gap-3 text-xs md:text-sm self-start md:self-center shadow-inner">
          <span className="relative flex h-2 w-2">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span className="text-slate-400">System Status:</span>
          <HealthStatus />
        </div>
      </header>

      {/* Main Skeleton Blocks */}
      <main className="grid md:grid-cols-3 gap-6">
        {/* Card 1 */}
        <div className="bg-slate-900/60 border border-slate-800/60 p-6 rounded-2xl relative overflow-hidden group hover:border-slate-700/60 transition-all duration-300">
          <div className="absolute top-0 right-0 w-32 h-32 bg-blue-500/5 rounded-full blur-2xl"></div>
          <div className="bg-blue-950/50 w-12 h-12 rounded-xl flex items-center justify-center text-blue-400 mb-4 border border-blue-800/20">
            <Database className="w-6 h-6" />
          </div>
          <h3 className="text-lg font-semibold text-slate-200">Internal Catalog</h3>
          <p className="text-slate-400 text-sm mt-2 leading-relaxed">
            Consolidated product database linking internal sales feedback channels and product reviews.
          </p>
          <div className="mt-4 pt-4 border-t border-slate-800/50 flex items-center text-xs text-slate-500 font-medium">
            Table status: Ready
          </div>
        </div>

        {/* Card 2 */}
        <div className="bg-slate-900/60 border border-slate-800/60 p-6 rounded-2xl relative overflow-hidden group hover:border-slate-700/60 transition-all duration-300">
          <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-500/5 rounded-full blur-2xl"></div>
          <div className="bg-indigo-950/50 w-12 h-12 rounded-xl flex items-center justify-center text-indigo-400 mb-4 border border-indigo-800/20">
            <Radio className="w-6 h-6" />
          </div>
          <h3 className="text-lg font-semibold text-slate-200">External Market Feed</h3>
          <p className="text-slate-400 text-sm mt-2 leading-relaxed">
            Reddit API connection listeners gathering subreddit discussions, upvotes, and post titles.
          </p>
          <div className="mt-4 pt-4 border-t border-slate-800/50 flex items-center text-xs text-slate-500 font-medium">
            API status: Configured
          </div>
        </div>

        {/* Card 3 */}
        <div className="bg-slate-900/60 border border-slate-800/60 p-6 rounded-2xl relative overflow-hidden group hover:border-slate-700/60 transition-all duration-300">
          <div className="absolute top-0 right-0 w-32 h-32 bg-violet-500/5 rounded-full blur-2xl"></div>
          <div className="bg-violet-950/50 w-12 h-12 rounded-xl flex items-center justify-center text-violet-400 mb-4 border border-violet-800/20">
            <Activity className="w-6 h-6" />
          </div>
          <h3 className="text-lg font-semibold text-slate-200">Sentiment Analyzer</h3>
          <p className="text-slate-400 text-sm mt-2 leading-relaxed">
            Natural Language Processing module measuring text polarity and tracking positive/negative discrepancies.
          </p>
          <div className="mt-4 pt-4 border-t border-slate-800/50 flex items-center text-xs text-slate-500 font-medium">
            NLP Engine: VADER Loaded
          </div>
        </div>
      </main>

      {/* Footer Info */}
      <footer className="text-center text-xs text-slate-600 mt-12">
        &copy; 2026 InsightBridge. Created & Configured under Stage 1 Architecture parameters.
      </footer>
    </div>
  )
}

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Dashboard />
    </QueryClientProvider>
  )
}
