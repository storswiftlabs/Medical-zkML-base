program dt.aleo {
	struct Inputs {
		p1: u32,
		p2: u32,
		p3: u32,
		p4: u32,
		p5: u32,
		p6: u32,
		p7: u32,
		p8: u32,
		p9: u32,
		p10: u32,
		p11: u32,
		p12: u32,
		p13: u32,
	}
	// Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py 
	transition main(inputs: Inputs) -> public u32 {
		if (inputs.p13 < 5u32) {
			if (inputs.p8 < 120u32) {
				if (inputs.p4 <= 134u32) {
					if (inputs.p7 <= 1u32) {
						if (inputs.p3 < 4u32) {
							return 0u32;
						} else {
							return 2u32;
						}
					} else {
						if (inputs.p5 < 261u32) {
							return 3u32;
						} else {
							if (inputs.p10 < 3u32) {
								return 1u32;
							} else {
								return 3u32;
							}
						}
					}
				} else {
					return 2u32;
				}
			} else {
				if (inputs.p10 < 3u32) {
					if (inputs.p1 < 56u32) {
						if (inputs.p4 <= 119u32) {
							if (inputs.p12 < 1u32) {
								if (inputs.p8 < 153u32) {
									if (inputs.p8 < 148u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								} else {
									return 0u32;
								}
							} else {
								if (inputs.p2 < 1u32) {
									return 0u32;
								} else {
									if (inputs.p5 <= 260u32) {
										return 1u32;
									} else {
										return 2u32;
									}
								}
							}
						} else {
							return 0u32;
						}
					} else {
						if (inputs.p11 < 2u32) {
							if (inputs.p10 < 1u32) {
								if (inputs.p10 < 1u32) {
									if (inputs.p4 <= 147u32) {
										if (inputs.p5 < 319u32) {
											return 0u32;
										} else {
											if (inputs.p7 <= 1u32) {
												return 1u32;
											} else {
												return 3u32;
											}
										}
									} else {
										if (inputs.p1 <= 62u32) {
											return 1u32;
										} else {
											return 0u32;
										}
									}
								} else {
									return 2u32;
								}
							} else {
								return 0u32;
							}
						} else {
							if (inputs.p12 < 1u32) {
								if (inputs.p9 < 1u32) {
									if (inputs.p10 < 2u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								} else {
									if (inputs.p2 < 1u32) {
										return 1u32;
									} else {
										return 0u32;
									}
								}
							} else {
								if (inputs.p8 < 138u32) {
									if (inputs.p9 < 1u32) {
										return 0u32;
									} else {
										return 3u32;
									}
								} else {
									return 1u32;
								}
							}
						}
					}
				} else {
					if (inputs.p1 < 61u32) {
						return 1u32;
					} else {
						if (inputs.p2 < 1u32) {
							return 3u32;
						} else {
							if (inputs.p9 < 1u32) {
								return 2u32;
							} else {
								return 4u32;
							}
						}
					}
				}
			}
		} else {
			if (inputs.p10 < 1u32) {
				if (inputs.p12 < 1u32) {
					if (inputs.p1 <= 42u32) {
						return 1u32;
					} else {
						if (inputs.p5 < 269u32) {
							return 0u32;
						} else {
							if (inputs.p8 < 158u32) {
								return 0u32;
							} else {
								if (inputs.p4 <= 147u32) {
									return 3u32;
								} else {
									return 1u32;
								}
							}
						}
					}
				} else {
					if (inputs.p7 <= 1u32) {
						if (inputs.p1 < 58u32) {
							if (inputs.p5 <= 244u32) {
								return 0u32;
							} else {
								return 1u32;
							}
						} else {
							if (inputs.p8 < 113u32) {
								return 0u32;
							} else {
								return 2u32;
							}
						}
					} else {
						if (inputs.p1 <= 51u32) {
							return 3u32;
						} else {
							return 1u32;
						}
					}
				}
			} else {
				if (inputs.p8 < 134u32) {
					if (inputs.p10 < 3u32) {
						if (inputs.p4 <= 129u32) {
							if (inputs.p8 < 128u32) {
								if (inputs.p4 < 124u32) {
									if (inputs.p13 < 7u32) {
										return 0u32;
									} else {
										return 3u32;
									}
								} else {
									return 1u32;
								}
							} else {
								if (inputs.p2 < 1u32) {
									return 3u32;
								} else {
									return 1u32;
								}
							}
						} else {
							if (inputs.p10 < 2u32) {
								if (inputs.p12 < 3u32) {
									if (inputs.p5 <= 272u32) {
										return 3u32;
									} else {
										if (inputs.p4 <= 141u32) {
											return 3u32;
										} else {
											return 1u32;
										}
									}
								} else {
									return 4u32;
								}
							} else {
								if (inputs.p5 < 249u32) {
									if (inputs.p8 <= 115u32) {
										return 1u32;
									} else {
										return 4u32;
									}
								} else {
									return 2u32;
								}
							}
						}
					} else {
						return 3u32;
					}
				} else {
					if (inputs.p10 < 2u32) {
						if (inputs.p3 < 4u32) {
							if (inputs.p6 < 1u32) {
								if (inputs.p1 <= 52u32) {
									if (inputs.p3 < 2u32) {
										return 0u32;
									} else {
										return 1u32;
									}
								} else {
									return 0u32;
								}
							} else {
								if (inputs.p13 < 7u32) {
									return 2u32;
								} else {
									return 3u32;
								}
							}
						} else {
							if (inputs.p5 <= 238u32) {
								if (inputs.p7 <= 1u32) {
									return 3u32;
								} else {
									return 1u32;
								}
							} else {
								if (inputs.p11 < 2u32) {
									return 1u32;
								} else {
									if (inputs.p8 < 147u32) {
										if (inputs.p2 < 1u32) {
											return 1u32;
										} else {
											return 4u32;
										}
									} else {
										return 2u32;
									}
								}
							}
						}
					} else {
						if (inputs.p8 <= 150u32) {
							if (inputs.p4 < 126u32) {
								if (inputs.p8 < 140u32) {
									return 3u32;
								} else {
									if (inputs.p11 < 3u32) {
										if (inputs.p4 < 118u32) {
											return 2u32;
										} else {
											return 1u32;
										}
									} else {
										return 4u32;
									}
								}
							} else {
								if (inputs.p11 < 2u32) {
									if (inputs.p12 <= 1u32) {
										return 0u32;
									} else {
										return 2u32;
									}
								} else {
									return 2u32;
								}
							}
						} else {
							if (inputs.p5 < 217u32) {
								return 1u32;
							} else {
								return 4u32;
							}
						}
					}
				}
			}
		}
	}
}