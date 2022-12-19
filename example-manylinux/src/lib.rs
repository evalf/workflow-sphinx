use pyo3::prelude::*;

/// Example
#[pymodule]
fn example(_py: Python, _m: &PyModule) -> PyResult<()> {
    Ok(())
}
