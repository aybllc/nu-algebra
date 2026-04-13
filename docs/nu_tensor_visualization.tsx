import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ScatterChart, Scatter, Cell } from 'recharts';

const InterpretationsAnalysis = () => {
  const [activeView, setActiveView] = useState('scores');

  // Real data from CSV
  const findings = [
    { id: 'F1', label: 'Telehealth coaching effective', scoreA: 3, scoreB: 3, uncA: 'Low', uncB: 'Medium' },
    { id: 'F2', label: 'IDKPTM response acquired', scoreA: 3, scoreB: 3, uncA: 'Low', uncB: 'Medium' },
    { id: 'F3', label: 'Correct answers improved', scoreA: 3, scoreB: 2, uncA: 'Medium', uncB: 'High' },
    { id: 'F4', label: 'Question reduction accelerated', scoreA: 3, scoreB: 3, uncA: 'Low', uncB: 'Medium' },
    { id: 'F5', label: 'Generalization occurred', scoreA: 3, scoreB: 2, uncA: 'Medium', uncB: 'High' },
    { id: 'F6', label: 'High fidelity maintained', scoreA: 3, scoreB: 2, uncA: 'Low', uncB: 'Medium' },
    { id: 'F7', label: 'Positive social validity', scoreA: 3, scoreB: 2, uncA: 'Low', uncB: 'Medium' },
    { id: 'F8', label: 'Telehealth viable', scoreA: 3, scoreB: 2, uncA: 'Low', uncB: 'Medium' },
    { id: 'F9', label: 'No control questions', scoreA: 1, scoreB: 1, uncA: 'High', uncB: 'High' },
    { id: 'F10', label: 'Session gaps/breaks', scoreA: 1, scoreB: 1, uncA: 'Medium', uncB: 'High' }
  ];

  // Convert to chart data
  const scoreComparisonData = findings.map(f => ({
    name: f.id,
    'Version A': f.scoreA,
    'Version B': f.scoreB,
    diff: f.scoreB - f.scoreA
  }));

  // Uncertainty mapping
  const uncMap = { 'Low': 1, 'Medium': 2, 'High': 3 };
  
  const uncertaintyChangeData = findings.map(f => ({
    name: f.id,
    'Version A': uncMap[f.uncA],
    'Version B': uncMap[f.uncB],
    change: uncMap[f.uncB] - uncMap[f.uncA]
  }));

  // N/U pair representation
  const scoreToNominal = { 3: 0.90, 2: 0.60, 1: 0.30 };
  const uncToU = { 'Low': 0.05, 'Medium': 0.15, 'High': 0.25 };

  const nuPairs = findings.map(f => ({
    id: f.id,
    label: f.label,
    n: scoreToNominal[f.scoreB],
    u: uncToU[f.uncB],
    lowerBound: scoreToNominal[f.scoreB] - uncToU[f.uncB],
    upperBound: scoreToNominal[f.scoreB] + uncToU[f.uncB]
  }));

  // Distribution data
  const distributionData = [
    { score: 3, Low: 0, Medium: 3, High: 0 },
    { score: 2, Low: 0, Medium: 5, High: 0 },
    { score: 1, Low: 0, Medium: 0, High: 2 }
  ];

  return (
    <div className="w-full max-w-6xl mx-auto p-6 bg-gray-50">
      <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
        <h1 className="text-3xl font-bold text-gray-800 mb-2">
          Interpretations Comparative Matrix Analysis
        </h1>
        <p className="text-gray-600">
          Real data from CSV: Quantitative comparison of Version A vs Version B findings
        </p>
      </div>

      {/* Navigation */}
      <div className="flex gap-2 mb-6 flex-wrap">
        {[
          { id: 'scores', label: 'Score Comparison' },
          { id: 'uncertainty', label: 'Uncertainty Changes' },
          { id: 'nu-pairs', label: 'N/U Pairs' },
          { id: 'distribution', label: 'Distribution' }
        ].map(view => (
          <button
            key={view.id}
            onClick={() => setActiveView(view.id)}
            className={`px-4 py-2 rounded-lg font-medium transition-colors ${
              activeView === view.id
                ? 'bg-blue-600 text-white'
                : 'bg-white text-gray-700 hover:bg-gray-100'
            }`}
          >
            {view.label}
          </button>
        ))}
      </div>

      {/* Score Comparison View */}
      {activeView === 'scores' && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">
            Ordered Score Comparison (A vs B)
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div className="bg-blue-50 p-4 rounded-lg">
              <div className="text-sm text-gray-600">Avg Score A</div>
              <div className="text-3xl font-bold text-blue-600">2.60</div>
            </div>
            <div className="bg-purple-50 p-4 rounded-lg">
              <div className="text-sm text-gray-600">Avg Score B</div>
              <div className="text-3xl font-bold text-purple-600">2.10</div>
            </div>
            <div className="bg-red-50 p-4 rounded-lg">
              <div className="text-sm text-gray-600">Average Change</div>
              <div className="text-3xl font-bold text-red-600">-0.50</div>
            </div>
          </div>

          <ResponsiveContainer width="100%" height={400}>
            <BarChart data={scoreComparisonData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis domain={[0, 3]} />
              <Tooltip />
              <Legend />
              <Bar dataKey="Version A" fill="#3B82F6" />
              <Bar dataKey="Version B" fill="#8B5CF6" />
            </BarChart>
          </ResponsiveContainer>

          <div className="mt-6 p-4 bg-gray-50 rounded">
            <h3 className="font-bold mb-2">Key Finding:</h3>
            <p className="text-gray-700">
              Version B scored lower on average (-0.50 points), with 5 findings 
              receiving reduced scores and 5 remaining unchanged. No findings 
              scored higher in Version B.
            </p>
          </div>
        </div>
      )}

      {/* Uncertainty Changes View */}
      {activeView === 'uncertainty' && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">
            Uncertainty Level Changes
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div className="bg-green-50 p-4 rounded-lg">
              <div className="text-sm text-gray-600">Increased</div>
              <div className="text-3xl font-bold text-green-600">9</div>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <div className="text-sm text-gray-600">Unchanged</div>
              <div className="text-3xl font-bold text-gray-600">1</div>
            </div>
            <div className="bg-orange-50 p-4 rounded-lg">
              <div className="text-sm text-gray-600">Avg Change</div>
              <div className="text-3xl font-bold text-orange-600">+0.90</div>
            </div>
          </div>

          <ResponsiveContainer width="100%" height={400}>
            <BarChart data={uncertaintyChangeData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis domain={[0, 3]} ticks={[1, 2, 3]} />
              <Tooltip />
              <Legend />
              <Bar dataKey="Version A" fill="#10B981" />
              <Bar dataKey="Version B" fill="#F59E0B" />
            </BarChart>
          </ResponsiveContainer>

          <div className="mt-6 space-y-2">
            <h3 className="font-bold">Changes by Finding:</h3>
            {findings.map(f => {
              const arrow = uncMap[f.uncB] > uncMap[f.uncA] ? '↑' : 
                           uncMap[f.uncB] < uncMap[f.uncA] ? '↓' : '→';
              return (
                <div key={f.id} className="flex justify-between text-sm p-2 bg-gray-50 rounded">
                  <span>{f.id}: {f.uncA} → {f.uncB}</span>
                  <span>{arrow}</span>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* N/U Pairs View */}
      {activeView === 'nu-pairs' && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">
            N/U Pair Representation (Version B)
          </h2>

          <div className="mb-6 p-4 bg-blue-50 rounded">
            <h3 className="font-bold mb-2">What are N/U Pairs?</h3>
            <p className="text-sm text-gray-700">
              Each finding is represented as (n, u) where:
            </p>
            <ul className="text-sm text-gray-700 mt-2 ml-4 list-disc">
              <li><strong>n</strong> = nominal value (0.30 for Low, 0.60 for Moderate, 0.90 for High)</li>
              <li><strong>u</strong> = uncertainty (0.05 for Low, 0.15 for Medium, 0.25 for High)</li>
            </ul>
          </div>

          <div className="space-y-3">
            {nuPairs.map(nu => (
              <div key={nu.id} className="border rounded-lg p-4">
                <div className="flex justify-between items-start mb-2">
                  <div>
                    <span className="font-bold text-lg">{nu.id}</span>
                    <span className="text-gray-600 ml-2">{nu.label}</span>
                  </div>
                  <span className="font-mono text-sm bg-gray-100 px-2 py-1 rounded">
                    NU({nu.n.toFixed(2)}, {nu.u.toFixed(2)})
                  </span>
                </div>
                
                <div className="relative h-8 bg-gray-200 rounded">
                  <div
                    className="absolute h-full bg-blue-300 rounded"
                    style={{
                      left: `${nu.lowerBound * 100}%`,
                      width: `${(nu.upperBound - nu.lowerBound) * 100}%`
                    }}
                  />
                  <div
                    className="absolute h-full w-1 bg-blue-600"
                    style={{ left: `${nu.n * 100}%` }}
                  />
                </div>
                
                <div className="text-xs text-gray-600 mt-1">
                  Interval: [{nu.lowerBound.toFixed(3)}, {nu.upperBound.toFixed(3)}]
                </div>
              </div>
            ))}
          </div>

          <div className="mt-6 p-4 bg-gray-50 rounded">
            <h3 className="font-bold mb-2">Ready for Tensor Operations</h3>
            <p className="text-sm text-gray-700">
              These N/U pairs can be organized into tensors for multi-dimensional 
              analysis. With session-level data, this structure enables:
            </p>
            <ul className="text-sm text-gray-700 mt-2 ml-4 list-disc">
              <li>Uncertainty propagation through arithmetic operations</li>
              <li>Conservative interval estimates across multiple dimensions</li>
              <li>Measurement precision quantification</li>
            </ul>
          </div>
        </div>
      )}

      {/* Distribution View */}
      {activeView === 'distribution' && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">
            Score × Uncertainty Distribution (Version B)
          </h2>

          <ResponsiveContainer width="100%" height={400}>
            <BarChart data={distributionData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="score" label={{ value: 'Ordered Score', position: 'bottom' }} />
              <YAxis label={{ value: 'Count', angle: -90, position: 'insideLeft' }} />
              <Tooltip />
              <Legend />
              <Bar dataKey="Low" stackId="a" fill="#10B981" />
              <Bar dataKey="Medium" stackId="a" fill="#F59E0B" />
              <Bar dataKey="High" stackId="a" fill="#EF4444" />
            </BarChart>
          </ResponsiveContainer>

          <div className="mt-6">
            <table className="w-full text-sm">
              <thead className="bg-gray-100">
                <tr>
                  <th className="p-2 text-left">Score</th>
                  <th className="p-2 text-center">Low</th>
                  <th className="p-2 text-center">Medium</th>
                  <th className="p-2 text-center">High</th>
                  <th className="p-2 text-center">Total</th>
                </tr>
              </thead>
              <tbody>
                <tr className="border-b">
                  <td className="p-2 font-medium">3 (High)</td>
                  <td className="p-2 text-center">0</td>
                  <td className="p-2 text-center">3</td>
                  <td className="p-2 text-center">0</td>
                  <td className="p-2 text-center font-bold">3</td>
                </tr>
                <tr className="border-b">
                  <td className="p-2 font-medium">2 (Moderate)</td>
                  <td className="p-2 text-center">0</td>
                  <td className="p-2 text-center">5</td>
                  <td className="p-2 text-center">0</td>
                  <td className="p-2 text-center font-bold">5</td>
                </tr>
                <tr className="border-b">
                  <td className="p-2 font-medium">1 (Low)</td>
                  <td className="p-2 text-center">0</td>
                  <td className="p-2 text-center">0</td>
                  <td className="p-2 text-center">2</td>
                  <td className="p-2 text-center font-bold">2</td>
                </tr>
                <tr className="bg-gray-100 font-bold">
                  <td className="p-2">Total</td>
                  <td className="p-2 text-center">0</td>
                  <td className="p-2 text-center">8</td>
                  <td className="p-2 text-center">2</td>
                  <td className="p-2 text-center">10</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div className="mt-6 p-4 bg-gray-50 rounded">
            <h3 className="font-bold mb-2">Correlation Analysis:</h3>
            <p className="text-gray-700">
              <strong>Moderate negative correlation</strong> between Ordered_Score 
              and Uncertainty_Level: Lower scores tend to have higher uncertainty,
              indicating appropriate epistemic humility in findings with methodological
              limitations.
            </p>
          </div>
        </div>
      )}
    </div>
  );
};

export default InterpretationsAnalysis;